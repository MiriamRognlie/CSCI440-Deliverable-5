import matplotlib.pyplot as plt
import scipy.stats
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from models.linear_model import linear_regression

def p3(db):
    # Question 3: Is​ ​the​ ​director’s​ ​popularity​ ​(based​ ​on​ ​Facebook​ ​likes)​ ​statistically​ ​correlated​
    # ​with​ ​the ratings​ ​or​ ​the​ ​profitability​ ​of​ ​a​ ​film?​
    # Run a query so "data" is a table containing the rating and Gross profit for each movie and the number of likes its director has on
    # Facebook
    data =  db.query(
        "select Rating, (cast(Revenue AS SIGNED) - cast(Budget AS SIGNED )) as gp, FacebookLikes from (movie join person_directs_movie on Movie_id=movie.id) where Rating is not NULL and Revenue is not NULL and Budget is not null and Country = 'USA'")
    #Analyze rating vs facebook likes
    x = data["FacebookLikes"].values.reshape(-1, 1)  # set up x an y axis for plotting data
    y = data["Rating"].values.reshape(-1, 1)
    # Lets
    # Lets create
    plt.figure(figsize=(16, 9))
    plt.scatter(x, y, marker='o', s=10.0)  # set up a scatter plot to display data found from query
    plt.plot(x, linear_regression(x, y), color='black',
             linewidth=2)  # displays a scatter plot popup window with the data from the queries and regression line
    plt.title("Director's Facebook Likes vs. Movie Rating")
    plt.xlabel("Director's Facebook Likes")
    plt.ylabel("Movie Rating (out of 10)")
    plt.savefig("p3-1.png", dpi=500)
    plt.show()

    #analyze data as profit vs facebook likes
    x = data["FacebookLikes"].values.reshape(-1, 1)  # set up x an y axis for plotting data
    y = data["gp"].values.reshape(-1, 1)
    # Lets create
    plt.figure(figsize=(16, 9))
    plt.scatter(x, y, marker='o', s=10.0)  # set up a scatter plot to display data found from query
    plt.plot(x, linear_regression(x, y), color='black',
             linewidth=2)  # displays a scatter plot popup window with the data from the queries and regression line
    plt.title("Director's Facebook Likes VS. Gross Profit")
    plt.xlabel("Director's Facebook Likes")
    plt.ylabel("Movie Profit (100 million dollars")
    plt.savefig("p3-2.png", dpi=500)
    plt.show()
