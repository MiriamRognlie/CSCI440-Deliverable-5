from sqlalchemy import create_engine
from mpl_toolkits.mplot3d import Axes3D

import pandas
import numpy
import matplotlib.pyplot as plt

#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')
conn = engine.connect()
conn.begin()
data = pandas.read_sql_query("select Runtime, (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country = 'USA'", conn)
data2 = pandas.read_sql_query("select Runtime, Rating from movie", conn)
#Lets create
plt.scatter(data["Runtime"], data["Profit"])
plt.show()
plt.scatter(data2["Runtime"], data2["Rating"])
plt.show()
# Plot colors.
#colors = ["#6BF8B8", "#547BEA", "#5E9C30", "#7B1B25", "#C925E8", "#6445DF", "#E335E1", "#030A03", "#A7FB22", "#1FB34A", "#CBF00C", "#FE034E", "#4524F2", "#89A85D", "#A6C691", "#16C06C", "#C6AC9F", "#BD4E23", "#1BDB42", "#8E9553", "#669260", "#F36A0F", "#9BDD90", "#1ABE6F"]
genres = pandas.read_sql_table("genre", conn)
print(genres)
for k, i in enumerate(genres["id"]):
    genre_grouped_profit = pandas.read_sql_query("select Runtime, (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit, genre_id from (movie join movie_has_genre on Movie_id=movie.id) where Country = 'USA' and genre_id=" + str(i), conn)
    plt.title("Movie Runtime vs. Gross Profit", fontsize='small')
    plt.scatter(genre_grouped_profit["Runtime"], genre_grouped_profit["Profit"], marker='o', label=genres["Name"][k])
plt.legend()
plt.show()