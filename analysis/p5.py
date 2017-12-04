import matplotlib.pyplot as plt

def p5(db):
    # Question 5: Over​ ​time,​ ​how​ ​has​ ​interest​ ​in​ ​specific​ ​genres​ ​changed​ ​for​ ​different​ ​regions​
    # ​around​ ​the world?​ ​What​ ​are​ ​the​ ​most​ ​popular​ ​genres​ ​now?​
    countries = db.query("SELECT DISTINCT Country FROM movie")#make a table containing all countries existing in the database, ordered by how many movies were made in each
    genres = db.table("genre")#make a table containing all the genres which exist in the database
    i = 1
    for country in countries["Country"]:#consider only movies made in hte first two countries, since samples from other countries are vary small
        if (i > 2):
            break
        i += 1
        print(country)
        for k, v in enumerate(genres["id"]):
            query = db.query(#Run a query so "query" is a table containing the Year a movie was made and the profit returned from the box office. Do this for each genre htat exists in the database
                "SELECT Year, GrossProfit FROM (movie JOIN movie_has_genre ON Movie_id=movie.id) WHERE revenue IS NOT NULL AND GrossProfit IS NOT NULL AND Country='" + country + "' AND Genre_id=" + str(
                    v) + " GROUP BY Year")
            plt.plot(query["Year"], query["GrossProfit"], label=genres["Name"][k])#create a line graph which displays each genre as a function of profit and year
        plt.title("Profitability of Genres in the " + country)#titles for graph and axis
        plt.xlabel("Year")
        plt.ylabel("Average Gross Profit")
        plt.legend()
        plt.show()
