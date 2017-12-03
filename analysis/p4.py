from sqlalchemy import create_engine
import pandas
import numpy as np
import matplotlib as mpl
#mpl.use('TkAgg')
import matplotlib.pyplot as plt
#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')
conn = engine.connect()
conn.begin()
data1 = pandas.read_sql_query("select (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country='USA' and ContentRating = 'G' and Budget is not null and GrossProfit is not null order by Profit desc", conn)
data2 = pandas.read_sql_query("select (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country='USA' and ContentRating = 'PG' and Budget is not null and GrossProfit is not null order by Profit desc", conn)
data3 = pandas.read_sql_query("select (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country='USA' and ContentRating = 'PG-13' and Budget is not null and GrossProfit is not null order by Profit desc", conn)
data4 = pandas.read_sql_query("select (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country='USA' and ContentRating = 'R' and Budget is not null and GrossProfit is not null order by Profit desc", conn)
data5 = pandas.read_sql_query("select (cast(GrossProfit as signed) - cast(Budget as signed )) as Profit from movie where Country='USA' and ContentRating = 'NC-17' and Budget is not null and GrossProfit is not null order by Profit desc", conn)
data = [data1["Profit"], data2["Profit"], data3["Profit"], data4["Profit"], data5["Profit"]]
fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)
bp = ax.boxplot(data, labels=["G", "PG", "PG-13", "R", "NC-17"])
plt.show()
fig.savefig('fig1.png', bbox_inches='tight')