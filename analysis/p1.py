import matplotlib.pyplot as plt
import scipy.stats
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sqlalchemy import create_engine

# Question 1: How​ ​is​ ​a​ ​movie’s​ ​budget​ ​related​ ​to​ ​the​ ​gross​ ​profit​ ​of​ ​a​ ​movie?​ ​Is​ ​there​
# ​a​ ​point​ ​where putting​ ​more​ ​money​ ​into​ ​a​ ​movie​ ​yields​ ​diminishing​ ​returns?​​ 
# Gross Profit as actually just revenue. Run a query so "data" is a table containing the Budget for amomvie and the
# profit returned from the box office.  This displayes only movies from the USA to ensure a common currency
data = db.query(
    "SELECT Budget, (cast(GrossProfit AS SIGNED) - cast(Budget AS SIGNED )) AS Profit FROM movie WHERE Country='USA' AND Budget IS NOT NULL AND GrossProfit IS NOT NULL")
x = data["Budget"].values.reshape(-1, 1)  # set up x an y axis for plotting data
y = data["Profit"].values.reshape(-1, 1)
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
         linewidth=2)  # displayes a scatter plot popup window with the data from the queries and regression line
plt.title("Movie Budget vs. Gross Profit in USA")
plt.xlabel("Movie Budget (100 million dollars)")
plt.ylabel("Gross Profit (100 million dollars)")
plt.show()
