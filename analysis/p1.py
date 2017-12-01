from sqlalchemy import create_engine
import pandas
import numpy as np
import matplotlib.pyplot as plt

#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')
conn = engine.connect()
conn.begin()
data = pandas.read_sql_query("select Budget, GrossProfit from movie where Country='USA'", conn)
#Lets
#Lets create
plt.scatter(data["Budget"], data["GrossProfit"])
plt.show()
print(data)