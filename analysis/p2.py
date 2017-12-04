import matplotlib.pyplot as plt
from scipy import stats
from sklearn import metrics
from sqlalchemy import create_engine
from sklearn import linear_model
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Question 2: Does​ ​the​ ​length​ ​of​ ​a​ ​movie​ ​affect​ ​its​ ​profitability​ ​or​ ​ratings?​ ​Is​ ​there​ ​a​ ​point​ ​where​ ​a movie​ ​is​ ​too​ ​short​ ​or​ ​too​ ​long?​ ​Is​ ​the​ ​optimal​ ​length​ ​of​ ​a​ ​movie​ ​influenced​ ​by​ ​its​ ​genre?
# Run a query so "data" is a table containing the runtime of all movies made in the USA and their profit (calculated as gross -budget)
data =  db.query(
    "SELECT Runtime, (cast(GrossProfit AS SIGNED) - cast(Budget AS SIGNED )) AS Profit FROM movie WHERE Country = 'USA' AND GrossProfit IS NOT NULL AND Budget IS NOT NULL and Runtime is not null order by Runtime")
# Run a query so "data2" is a table containing the runtime of all movies and their ratings
data2 = db.query("SELECT Runtime, Rating FROM movie WHERE Rating IS NOT NULL and Country = 'USA' and Runtime is not null ORDER BY Runtime")
# Lets create
plt.scatter(data["Runtime"], data["Profit"])  # set up a scatter plot to display data found from query
plt.title("Movie Runtime vs Gross Profit")
plt.xlabel("Runtime (minutes)")
plt.ylabel("Gross Profit (100 million dollars)")

x = data["Runtime"].reshape(-1, 1)
y = data["Profit"].reshape(-1, 1)

model = make_pipeline(PolynomialFeatures(3), Ridge())
model.fit(x, y)
y_plot = model.predict(x)
plt.plot(x, y_plot, color='black')

plt.show()

plt.scatter(data2["Runtime"], data2["Rating"])  # set up a scatter plot to display data2 found from query
plt.title("Movie Runtime vs. Rating")
plt.xlabel("Runtime (minutes)")
plt.ylabel("Rating")

x = data2["Runtime"].reshape(-1, 1)
y = data2["Rating"].reshape(-1, 1)

# Lets do some linear regression on the Runtime/Rating
regr = linear_model.LinearRegression()  # calculate regression line for this data
regr.fit(x, y)
pred = regr.predict(x)
# The coefficients
print('Regression Coefficient (Slope): \n',
      regr.coef_)  # prints out the regression line coefficients from the scatter plot
print('Pearson\'s Correlation: ', stats.pearsonr(x, y))  # calculates and prints Pearson's correlation coefficient
#  based on data from the scatter plot
print('Spearman\'s Correlation: ', stats.spearmanr(x, y))  # calculates and prints Spearman's rank correlation
# coefficient based on data from the scatter plot
print("Mean squared error: %.2f" % metrics.mean_squared_error(x, y))  # calculates and prints the mean squared error
plt.plot(x, pred, color='black',
         linewidth=2)  # displayes a scatter plot popup window with the data from the queries and regression line

plt.show()

genres = db.query("genre")  # read a list of all genres existing in database

for k, i in enumerate(genres["id"]):  # go through each genre that exists in the database
    genre_grouped_profit =  db.query(
        "SELECT Runtime, (cast(GrossProfit AS SIGNED) - cast(Budget AS SIGNED )) AS Profit, genre_id FROM (movie JOIN movie_has_genre ON Movie_id=movie.id) WHERE GrossProfit is not null and Budget is not null and Country = 'USA' and Runtime is not null AND genre_id=" + str(
            i))
    plt.scatter(genre_grouped_profit["Runtime"], genre_grouped_profit["Profit"], marker='o',
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