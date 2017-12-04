import matplotlib.pyplot as plt

def p5(db):
    # Question 5: Over​ ​time,​ ​how​ ​has​ ​interest​ ​in​ ​specific​ ​genres​ ​changed​ ​for​ ​different​ ​regions​
    # ​around​ ​the world?​ ​What​ ​are​ ​the​ ​most​ ​popular​ ​genres​ ​now?​
    countries = db.query("SELECT DISTINCT Country FROM movie")
    genres = db.table("genre")
    i = 1
    for country in countries["Country"]:
        if (i > 2):
            break
        i += 1
        print(country)
        for k, v in enumerate(genres["id"]):
            query = db.query(
                "SELECT Year, GrossProfit FROM (movie JOIN movie_has_genre ON Movie_id=movie.id) WHERE revenue IS NOT NULL AND GrossProfit IS NOT NULL AND Country='" + country + "' AND Genre_id=" + str(
                    v) + " GROUP BY Year")
            plt.plot(query["Year"], query["GrossProfit"], label=genres["Name"][k])
        plt.title("Profitability of Genres in the " + country)
        plt.xlabel("Year")
        plt.ylabel("Average Gross Profit")
        plt.legend()
        plt.show()
