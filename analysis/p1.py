from sqlalchemy import create_engine
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import scipy.stats

#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')
conn = engine.connect()
conn.begin()
data = pandas.read_sql_query("select Budget, GrossProfit from movie where Country='USA' and Budget is not null and GrossProfit is not null", conn)
x = data["Budget"].values.reshape(-1, 1)
y = data["GrossProfit"].values.reshape(-1, 1)
#Lets
#Lets create
plt.scatter(x, y, marker='o', s=1.0)
regr = linear_model.LinearRegression()
regr.fit(x, y)
pred = regr.predict(x)
# The coefficients
print('Regression Coefficient (Slope): \n', regr.coef_)
print('Pearson\'s Correlation: ', scipy.stats.pearsonr(x, y));
print('Spearman\'s Correlation: ', scipy.stats.spearmanr(x, y));
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(x, y))
plt.plot(x, pred, color='black', linewidth=2)
plt.show()