import matplotlib.pyplot as plt
import pandas
from sqlalchemy import create_engine

# Question 2: Does​ ​the​ ​length​ ​of​ ​a​ ​movie​ ​affect​ ​its​ ​profitability​ ​or​ ​ratings?​ ​Is​ ​there​ ​a​ ​point​ ​where​ ​a movie​ ​is​ ​too​ ​short​ ​or​ ​too​ ​long?​ ​Is​ ​the​ ​optimal​ ​length​ ​of​ ​a​ ​movie​ ​influenced​ ​by​ ​its​ ​genre?
# Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')  # create connection to our movie database
conn = engine.connect()
conn.begin()
# Run a query so "data" is a table containing the runtime of all movies made in the USA and their profit (calculated as gross -budget)
data = pandas.read_sql_query(
    "SELECT Runtime, (cast(GrossProfit AS SIGNED) - cast(Budget AS SIGNED )) AS Profit FROM movie WHERE Country = 'USA' AND GrossProfit IS NOT NULL AND Budget IS NOT NULL ",
    conn)
# Run a query so "data2" is a table containing the runtime of all movies and their ratings
data2 = pandas.read_sql_query("SELECT Runtime, Rating FROM movie WHERE Rating IS NOT NULL ", conn)
print(data)
print(data2)
# Lets create
plt.scatter(data["Runtime"], data["Profit"])  # set up a scatter plot to display data found from query
plt.show()
plt.scatter(data2["Runtime"], data2["Rating"])  # set up a scatter plot to display data2 found from query
plt.show()
genres = pandas.read_sql_table("genre", conn)  # read a list of all genres existing in database
print(genres)
for k, i in enumerate(genres["id"]):  # go through each genre that exists in the database
    genre_grouped_profit = pandas.read_sql_query(
        "SELECT Runtime, (cast(GrossProfit AS SIGNED) - cast(Budget AS SIGNED )) AS Profit, genre_id FROM (movie JOIN movie_has_genre ON Movie_id=movie.id) WHERE Country = 'USA' AND genre_id=" + str(
            i), conn)
    plt.scatter(genre_grouped_profit["Runtime"], genre_grouped_profit["Profit"], marker='o',
                label=genres["Name"][k])  # show a line for each genre
plt.title("Movie Runtime vs. Gross Profit", fontsize='small')
plt.legend()
plt.show()
