import matplotlib.pyplot as plt
import pandas
import scipy.stats
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sqlalchemy import create_engine

# Question 3: Is​ ​the​ ​director’s​ ​popularity​ ​(based​ ​on​ ​Facebook​ ​likes)​ ​statistically​ ​correlated​
# ​with​ ​the ratings​ ​or​ ​the​ ​profitability​ ​of​ ​a​ ​film?​ Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')  # create connection to our movie database
conn = engine.connect()
conn.begin()
# Run a query so "data" is a table containing the rating for each movie and the number of likes its director has on
# Facebook
data = pandas.read_sql_query(
    "select Rating, FacebookLikes from (movie join person_directs_movie on Movie_id=movie.id) where Rating is not null",
    conn)
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
