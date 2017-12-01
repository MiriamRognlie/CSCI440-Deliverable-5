from sqlalchemy import create_engine
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')
conn = engine.connect()
conn.begin()
data = pandas.read_sql_query("select Budget, GrossProfit from movie where Country='USA' and Budget is not null and GrossProfit is not null", conn)
#Lets
#Lets create
plt.scatter(data["Budget"], data["GrossProfit"])
regr = linear_model.LinearRegression()
#regr.fit(data["Budget"], data["GrossProfit"])
#pred = regr.predict(data)
# The coefficients
#print('Coefficients: \n', regr.coef_)
# The mean squared error
#print("Mean squared error: %.2f"
 #     % mean_squared_error(data["Budget"], data["GrossProfit"]))
#plt.plot(data["Budget"], pred, color='blue', linewidth=3)
plt.show()