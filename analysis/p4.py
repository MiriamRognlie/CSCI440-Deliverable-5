from sqlalchemy import create_engine
import pandas
import numpy as np
import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt

#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')
conn = engine.connect()
conn.begin()
data1 = pandas.read_sql_query("select GrossProfit from movie where Country='USA' and ContentRating = 'G'  and GrossProfit is not null order by GrossProfit desc", conn)
data2 = pandas.read_sql_query("select GrossProfit from movie where Country='USA' and ContentRating = 'PG' and GrossProfit is not null order by GrossProfit desc", conn)
data3 = pandas.read_sql_query("select GrossProfit from movie where Country='USA' and ContentRating = 'PG-13'  and GrossProfit is not null order by GrossProfit desc", conn)
data4 = pandas.read_sql_query("select GrossProfit from movie where Country='USA' and ContentRating = 'R'  and GrossProfit is not null order by GrossProfit desc", conn)
data5 = pandas.read_sql_query("select GrossProfit from movie where Country='USA' and ContentRating = 'NC-17'  and GrossProfit is not null order by GrossProfit desc", conn)
data = [data1["GrossProfit"], data2["GrossProfit"], data3["GrossProfit"], data4["GrossProfit"], data5["GrossProfit"]]
fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)
bp = ax.boxplot(data)
fig.show()
