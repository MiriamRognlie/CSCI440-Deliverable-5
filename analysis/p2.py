import matplotlib.pyplot as plt
from models.linear_model import linear_regression
from models.polynomial_model import ridge_regression

def p2(db):
    # Question 2: Does​ ​the​ ​length​ ​of​ ​a​ ​movie​ ​affect​ ​its​ ​profitability​ ​or​ ​ratings?​ ​Is​ ​there​ ​a​ ​point​ ​where​ ​a movie​ ​is​ ​too​ ​short​ ​or​ ​too​ ​long?​ ​Is​ ​the​ ​optimal​ ​length​ ​of​ ​a​ ​movie​ ​influenced​ ​by​ ​its​ ​genre?
    # Run a query so "data" is a table containing the runtime of all movies made in the USA and their profit (calculated as gross-budget, since GrossProfic was inaccurately names in the database)
    data =  db.query(
        "SELECT Runtime, (cast(Revenue AS SIGNED) - cast(Budget AS SIGNED )) AS GrossProfit FROM movie WHERE Country = 'USA' AND movie.Revenue IS NOT NULL AND Budget IS NOT NULL and Runtime is not null order by Runtime")
    # Run a query so "data2" is a table containing the runtime of all movies and their ratings
    data2 = db.query("SELECT Runtime, Rating FROM movie WHERE Rating IS NOT NULL and Country = 'USA' and Runtime is not null ORDER BY Runtime")
    # Lets create
    plt.scatter(data["Runtime"], data["GrossProfit"])  # set up a scatter plot to display data found from query
    plt.title("Movie Runtime vs Gross Profit")
    plt.xlabel("Runtime (minutes)")
    plt.ylabel("Gross Profit (100 million dollars)")

    x = data["Runtime"].reshape(-1, 1)
    y = data["GrossProfit"].reshape(-1, 1)
    pred = ridge_regression(x, y, 3)
    plt.plot(x, pred, color='black')

    plt.show()

    plt.scatter(data2["Runtime"], data2["Rating"])  # set up a scatter plot to display data2 found from query
    plt.title("Movie Runtime vs. Rating")
    plt.xlabel("Runtime (minutes)")
    plt.ylabel("Rating")

    x = data2["Runtime"].reshape(-1, 1)
    y = data2["Rating"].reshape(-1, 1)

    # Lets do some linear regression on the Runtime/Rating
    pred = linear_regression(x, y)
    plt.plot(x, pred, color='black',
             linewidth=2)  # displayes a scatter plot popup window with the data from the queries and regression line
    plt.show()

    genres = db.table("genre")  # read a list of all genres existing in database

    for k, i in enumerate(genres["id"]):  # go through each genre that exists in the database
        genre_grouped_profit =  db.query(
            "SELECT Runtime, (cast(Revenue AS SIGNED) - cast(Budget AS SIGNED )) AS GrossProfit, genre_id FROM (movie JOIN movie_has_genre ON Movie_id=movie.id) WHERE Revenue is not null and Budget is not null and Country = 'USA' and Runtime is not null AND genre_id=" + str(
                i))
        plt.scatter(genre_grouped_profit["Runtime"], genre_grouped_profit["GrossProfit"], marker='o',
                    label=genres["Name"][k])  # show a line for each genre
    plt.title("Movie Runtime vs. Gross Profit", fontsize='small')
    plt.xlabel("Runtime (minutes)")
    plt.ylabel("Gross Profit (100 million dollars)")
    plt.legend()
    plt.show()

    for k, i in enumerate(genres["id"]):  # go through each genre that exists in the database
        genre_grouped_rating =  db.query(
            "SELECT Runtime, Rating, genre_id FROM (movie JOIN movie_has_genre ON Movie_id=movie.id) WHERE Country = 'USA' and Rating is not null AND genre_id=" + str(
                i))
        plt.scatter(genre_grouped_rating["Runtime"], genre_grouped_rating["Rating"], marker='o',
                    label=genres["Name"][k])  # show a line for each genre
    plt.title("Movie Runtime vs. Rating", fontsize='small')
    plt.xlabel("Runtime (minutes)")
    plt.ylabel("Rating")
    plt.legend()
    plt.show()