from sqlalchemy import create_engine
import pandas
import numpy as np
import matplotlib as mpl
#mpl.use('TkAgg')
import matplotlib.pyplot as plt
#Question 4: Does​ ​content​ ​rating​ ​affect​ ​how​ ​many​ ​people​ ​will​ ​watch​ ​a​ ​movie?​ ​What​ ​content​ ​ratings are​ ​the​ ​safest​ ​for​ ​a​ ​movie?​
#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')#create connection to our movie database
conn = engine.connect()
conn.begin()
#Run a query so "data1" is a table containing the profit for all movies made in the USA with a content rating of G
data1 = pandas.read_sql_query("select (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country='USA' and ContentRating = 'G' and Budget is not null and GrossProfit is not null order by Profit desc", conn)
#Run a query so "data2" is a table containing the profit for all movies made in the USA with a content rating of PG
data2 = pandas.read_sql_query("select (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country='USA' and ContentRating = 'PG' and Budget is not null and GrossProfit is not null order by Profit desc", conn)
#Run a query so "data3" is a table containing the profit for all movies made in the USA with a content rating of PG-13
data3 = pandas.read_sql_query("select (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country='USA' and ContentRating = 'PG-13' and Budget is not null and GrossProfit is not null order by Profit desc", conn)
#Run a query so "data4" is a table containing the profit for all movies made in the USA with a content rating of R
data4 = pandas.read_sql_query("select (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country='USA' and ContentRating = 'R' and Budget is not null and GrossProfit is not null order by Profit desc", conn)
#Run a query so "data5" is a table containing the profit for all movies made in the USA with a content rating of NC-17
data5 = pandas.read_sql_query("select (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country='USA' and ContentRating = 'NC-17' and Budget is not null and GrossProfit is not null order by Profit desc", conn)
data = [data1["Profit"], data2["Profit"], data3["Profit"], data4["Profit"], data5["Profit"]]#combine all these tables into one
fig = plt.figure(1, figsize=(9, 6))#set up a box and whicker plot to show this data
ax = fig.add_subplot(111)
bp = ax.boxplot(data, labels=["G", "PG", "PG-13", "R", "NC-17"])#create labels for the plot
plt.show()
fig.savefig('fig1.png', bbox_inches='tight')#save this plot