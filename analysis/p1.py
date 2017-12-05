import matplotlib.pyplot as plt
from models.linear_model import linear_regression

def p1(db):
    # Question 1: How​ ​is​ ​a​ ​movie’s​ ​budget​ ​related​ ​to​ ​the​ ​gross​ ​profit​ ​of​ ​a​ ​movie?​ ​Is​ ​there​
    # ​a​ ​point​ ​where putting​ ​more​ ​money​ ​into​ ​a​ ​movie​ ​yields​ ​diminishing​ ​returns?​​
    # Gross Profit as actually just revenue. Run a query so "data" is a table containing the Budget for amomvie and the
    # profit returned from the box office.  This displayes only movies from the USA to ensure a common currency
    data = db.query(
        "SELECT Budget, (cast(Revenue AS SIGNED) - cast(Budget AS SIGNED )) AS GrossProfit FROM movie WHERE Country='USA' AND Budget IS NOT NULL AND movie.Revenue IS NOT NULL ORDER BY Budget")
    x = data["Budget"].values.reshape(-1, 1)  # set up x an y axis for plotting data
    y = data["GrossProfit"].values.reshape(-1, 1)
    plt.scatter(x, y, marker='o', s=1.0)  # set up a scatter plot to display data found from query

    plt.plot(x, linear_regression(x, y), color='black',
             linewidth=3)  # displayes a scatter plot popup window with the data from the queries and regression line
    plt.title("Movie Budget vs. Gross Profit in USA")
    plt.xlabel("Movie Budget (100 million dollars)")
    plt.ylabel("Gross Profit (100 million dollars)")
    plt.show()