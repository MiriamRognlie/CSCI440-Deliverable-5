from sqlalchemy import create_engine
from mpl_toolkits.mplot3d import Axes3D

import pandas
import numpy
import matplotlib.pyplot as plt

#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')
conn = engine.connect()
conn.begin()
data = pandas.read_sql_query("select Runtime, GrossProfit from movie where Country = 'USA'", conn)
data2 = pandas.read_sql_query("select Runtime, Rating from movie", conn)
#Lets
#Lets create
plt.scatter(data["Runtime"], data["GrossProfit"])
plt.show()
plt.scatter(data2["Runtime"], data2["Rating"])
plt.show()

print(data)