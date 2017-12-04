import matplotlib.pyplot as plt
import scipy.stats
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

def p3(db):
    # Question 3: Is​ ​the​ ​director’s​ ​popularity​ ​(based​ ​on​ ​Facebook​ ​likes)​ ​statistically​ ​correlated​
    # ​with​ ​the ratings​ ​or​ ​the​ ​profitability​ ​of​ ​a​ ​film?​
    # Run a query so "data" is a table containing the rating and Gross profit for each movie and the number of likes its director has on
    # Facebook
    data =  db.query(
        "select Rating, GrossProfit, FacebookLikes from (movie join person_directs_movie on Movie_id=movie.id) where Rating is not NULL and GrossProfit is not NULL and Country = 'USA'")
    #Analyze rating vs facebook likes
    x = data["Rating"].values.reshape(-1, 1)  # set up x an y axis for plotting data
    y = data["FacebookLikes"].values.reshape(-1, 1)
    # Lets
    # Lets create
    plt.scatter(x, y, marker='o', s=1.0)  # set up a scatter plot to display data found from query
    regr = linear_model.LinearRegression()  # calculate regression line for this data
    regr.fit(x, y)
    pred = regr.predict(x)
    # The coefficients
    print('Regression Coefficient (Slope): \n',
          regr.coef_)  # prints out the regression line coefficients from the scatter plot
    print('Pearson\'s Correlation: ', scipy.stats.pearsonr(x,
                                                           y))  # calculates and prints Pearson's correlation coefficient
    #  based on data from the scatter plot
    print('Spearman\'s Correlation: ', scipy.stats.spearmanr(x,
                                                             y))  # calculates and prints Spearman's rank correlation
    # coefficient based on data from the scatter plot
    print("Mean squared error: %.2f" % mean_squared_error(x, y))  # calculates and prints the mean squared error
    plt.plot(x, pred, color='black',
             linewidth=2)  # displays a scatter plot popup window with the data from the queries and regression line
    plt.title("Movie Rating vs. Director's Facebook Likes")
    plt.xlabel("Movie Rating (out of 10)")
    plt.ylabel("Director's Facebook Likes")
    plt.show()
    #analyze data as profit vs facebook likes
    x = data["GrossProfit"].values.reshape(-1, 1)  # set up x an y axis for plotting data
    y = data["FacebookLikes"].values.reshape(-1, 1)
    # Lets
    # Lets create
    plt.scatter(x, y, marker='o', s=1.0)  # set up a scatter plot to display data found from query
    regr = linear_model.LinearRegression()  # calculate regression line for this data
    regr.fit(x, y)
    pred = regr.predict(x)
    # The coefficients
    print('Regression Coefficient (Slope): \n',
          regr.coef_)  # prints out the regression line coefficients from the scatter plot
    print('Pearson\'s Correlation: ', scipy.stats.pearsonr(x, y))  # calculates and prints Pearson's correlation coefficient
    #  based on data from the scatter plot
    print('Spearman\'s Correlation: ', scipy.stats.spearmanr(x, y))  # calculates and prints Spearman's rank correlation
    # coefficient based on data from the scatter plot
    print("Mean squared error: %.2f" % mean_squared_error(x, y))  # calculates and prints the mean squared error
    plt.plot(x, pred, color='black',
             linewidth=2)  # displays a scatter plot popup window with the data from the queries and regression line
    plt.title("Movie Profit vs. Director's Facebook Likes")
    plt.xlabel("Movie Profit (100 million dollars")
    plt.ylabel("Director's Facebook Likes")
    plt.show()
