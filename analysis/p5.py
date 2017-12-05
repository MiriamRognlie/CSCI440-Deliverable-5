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
            query = db.query(
                "select Year, avg(cast(Revenue AS SIGNED) - cast(Budget AS SIGNED )) as AverageProfit from (movie JOIN movie_has_genre ON Movie_id=movie.id) WHERE budget IS NOT NULL AND movie.Revenue IS NOT NULL AND Country='" + country + "' AND Genre_id=" + str(
                    v) + " GROUP BY Year order by year")
            plt.plot(query["Year"], query["AverageProfit"], label=genres["Name"][k])
        plt.title("Profitability of Genres in the " + country)
        plt.xlabel("Year")
        plt.ylabel("Average Gross Profit (100 millions)")
        plt.legend()
        plt.show()

    opt = ""
    colors = ["blue", "red"]
    while opt != "exit":
        try:
            gid = genres["id"][int(opt)]
            i = 1
            for country in countries["Country"]:
                if (i > 2):
                    break
                i += 1
                query = db.query(
                        "select Year, avg(cast(Revenue AS SIGNED) - cast(Budget AS SIGNED )) as AverageProfit from (movie JOIN movie_has_genre ON Movie_id=movie.id) WHERE budget IS NOT NULL AND movie.Revenue IS NOT NULL AND Country='" + country + "' AND Genre_id=" + str(gid) + " GROUP BY Year order by year")
                plt.plot(query["Year"], query["AverageProfit"], label=country)
                scatter_query = db.query("select Year, (cast(Revenue AS SIGNED) - cast(Budget AS SIGNED)) as grossProfit from (movie JOIN movie_has_genre ON Movie_id=movie.id) WHERE budget is not null and movie.Revenue is not null and Country='" + country +"' and Genre_id=" + str(gid) + " order by year")
                plt.scatter(scatter_query["Year"], scatter_query["grossProfit"], label='_nolegend_')
            plt.legend()
            plt.xlabel("Year")
            plt.ylabel("Gross Profit (100 millions) [Lines are averaged by year]")
            plt.title("Profitability of " + genres["Name"][int(opt)])
            plt.show()
        except:
            pass
        print("This data is available by genre as scatter plots for a single genre:")
        for k,v in enumerate(genres["Name"]):
            print("\t", k, ": ", v)
        print("\t exit: Go back to problem selection.")
        opt = input("Your Choice > ")