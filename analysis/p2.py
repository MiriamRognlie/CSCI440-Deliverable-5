from sqlalchemy import create_engine
from mpl_toolkits.mplot3d import Axes3D

import pandas
import numpy
import matplotlib.pyplot as plt
#Question 2: Does​ ​the​ ​length​ ​of​ ​a​ ​movie​ ​affect​ ​its​ ​profitability​ ​or​ ​ratings?​ ​Is​ ​there​ ​a​ ​point​ ​where​ ​a movie​ ​is​ ​too​ ​short​ ​or​ ​too​ ​long?​ ​Is​ ​the​ ​optimal​ ​length​ ​of​ ​a​ ​movie​ ​influenced​ ​by​ ​its​ ​genre?
#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')#create connection to our movie database
conn = engine.connect()
conn.begin()
#Run a query so "data" is a table containing the runtime of all movies made in the USA and their profit (calculated as gross -budget)
data = pandas.read_sql_query("select Runtime, (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country = 'USA' and GrossProfit is not NULL and Budget is not NULL ", conn)
#Run a query so "data2" is a table containing the runtime of all movies and their ratings
data2 = pandas.read_sql_query("select Runtime, Rating from movie where Rating is not NULL ", conn)
print(data)
print(data2)
#Lets create
plt.scatter(data["Runtime"], data["Profit"])#set up a scatter plot to display data found from query
plt.show()
plt.scatter(data2["Runtime"], data2["Rating"])#set up a scatter plot to display data2 found from query
plt.show()
# Plot colors.
#colors = ["#6BF8B8", "#547BEA", "#5E9C30", "#7B1B25", "#C925E8", "#6445DF", "#E335E1", "#030A03", "#A7FB22", "#1FB34A", "#CBF00C", "#FE034E", "#4524F2", "#89A85D", "#A6C691", "#16C06C", "#C6AC9F", "#BD4E23", "#1BDB42", "#8E9553", "#669260", "#F36A0F", "#9BDD90", "#1ABE6F"]
genres = pandas.read_sql_table("genre", conn)#read a list of all genres existing in database
print(genres)
for k, i in enumerate(genres["id"]):#go through each genre that exists in the database
    genre_grouped_profit = pandas.read_sql_query("select Runtime, (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit, genre_id from (movie join movie_has_genre on Movie_id=movie.id) where Country = 'USA' and genre_id=" + str(i), conn)
    plt.title("Movie Runtime vs. Gross Profit", fontsize='small')
    plt.scatter(genre_grouped_profit["Runtime"], genre_grouped_profit["Profit"], marker='o', label=genres["Name"][k])#show a line for each genre
plt.legend()
plt.show()