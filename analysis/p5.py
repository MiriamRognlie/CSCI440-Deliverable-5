import matplotlib.pyplot as plt
import pandas
from sqlalchemy import create_engine

# Question 5: Over​ ​time,​ ​how​ ​has​ ​interest​ ​in​ ​specific​ ​genres​ ​changed​ ​for​ ​different​ ​regions​
# ​around​ ​the world?​ ​What​ ​are​ ​the​ ​most​ ​popular​ ​genres​ ​now?​ Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')  # create connection to our movie database
conn = engine.connect()
conn.begin()
countries = pandas.read_sql_query("SELECT DISTINCT Country FROM movie", conn)
genres = pandas.read_sql_table("genre", conn)
i = 1
for country in countries["Country"]:
    if (i > 2):
        break
    i += 1
    print(country)
    for k, v in enumerate(genres["id"]):
        query = pandas.read_sql_query(
            "SELECT Year, GrossProfit FROM (movie JOIN movie_has_genre ON Movie_id=movie.id) WHERE revenue IS NOT NULL AND GrossProfit IS NOT NULL AND Country='" + country + "' AND Genre_id=" + str(
                v) + " GROUP BY Year", conn)
        plt.plot(query["Year"], query["GrossProfit"], label=genres["Name"][k])
        print(query)
    plt.title("Profitability of Genres in the " + country)
    plt.legend()
    plt.show()
