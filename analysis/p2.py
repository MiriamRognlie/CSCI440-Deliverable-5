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

genres = pandas.read_sql_table("genre", conn)
print(genres)
for k, i in enumerate(genres["id"]):
    genre_grouped_profit = pandas.read_sql_query("select Runtime, (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit, genre_id from (movie join movie_has_genre on Movie_id=movie.id) where Country = 'USA' and genre_id=" + str(i), conn)
    plt.scatter(genre_grouped_profit["Runtime"], genre_grouped_profit["Profit"], marker='o', label=genres["Name"][k])
plt.title("Movie Runtime vs. Gross Profit", fontsize='small')
plt.legend()
plt.show()