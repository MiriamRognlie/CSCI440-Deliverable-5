from sqlalchemy import create_engine
import pandas
import numpy
import matplotlib.pyplot as plt

#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')
conn = engine.connect()
conn.begin()
countries = pandas.read_sql_query("SELECT DISTINCT Country from movie", conn)
genres = pandas.read_sql_table("genre", conn)
i = 1
for country in countries["Country"]:
    if(i > 2):
        break
    i+=1
    print(country)
    for k, v in enumerate(genres["id"]):
        query = pandas.read_sql_query("SELECT Year, GrossProfit FROM (movie join movie_has_genre on Movie_id=movie.id) where revenue is not null and GrossProfit is not null and Country='"+ country + "' and Genre_id=" + str(v) + " group BY Year", conn)
        plt.plot(query["Year"], query["GrossProfit"], label=genres["Name"][k])
        print(query)
    plt.title("Profitability of Genres in the " + country)
    plt.legend()
    plt.show()
