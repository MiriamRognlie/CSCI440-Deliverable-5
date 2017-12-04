# mpl.use('TkAgg')
import matplotlib.pyplot as plt
import pandas
import scipy
from sqlalchemy import create_engine

# Question 4: Does​ ​content​ ​rating​ ​affect​ ​how​ ​many​ ​people​ ​will​ ​watch​ ​a​ ​movie?​ ​What​ ​content​
# ​ratings are​ ​the​ ​safest​ ​for​ ​a​ ​movie?​ Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')  # create connection to our movie database
conn = engine.connect()
conn.begin()
# Run a query so "data1" is a table containing the profit for all movies made in the USA with a content rating of G
data1 = pandas.read_sql_query(
    "SELECT (cast(GrossProfit AS SIGNED) - cast(Budget AS SIGNED )) AS Profit FROM movie WHERE Country='USA' AND ContentRating = 'G' AND Budget IS NOT NULL AND GrossProfit IS NOT NULL ORDER BY Profit DESC",
    conn)
# Run a query so "data2" is a table containing the profit for all movies made in the USA with a content rating of PG
data2 = pandas.read_sql_query(
    "SELECT (cast(GrossProfit AS SIGNED) - cast(Budget AS SIGNED )) AS Profit FROM movie WHERE Country='USA' AND ContentRating = 'PG' AND Budget IS NOT NULL AND GrossProfit IS NOT NULL ORDER BY Profit DESC",
    conn)
# Run a query so "data3" is a table containing the profit for all movies made in the USA with a content rating of PG-13
data3 = pandas.read_sql_query(
    "SELECT (cast(GrossProfit AS SIGNED) - cast(Budget AS SIGNED )) AS Profit FROM movie WHERE Country='USA' AND ContentRating = 'PG-13' AND Budget IS NOT NULL AND GrossProfit IS NOT NULL ORDER BY Profit DESC",
    conn)
# Run a query so "data4" is a table containing the profit for all movies made in the USA with a content rating of R
data4 = pandas.read_sql_query(
    "SELECT (cast(GrossProfit AS SIGNED) - cast(Budget AS SIGNED )) AS Profit FROM movie WHERE Country='USA' AND ContentRating = 'R' AND Budget IS NOT NULL AND GrossProfit IS NOT NULL ORDER BY Profit DESC",
    conn)
# Run a query so "data5" is a table containing the profit for all movies made in the USA with a content rating of NC-17
data5 = pandas.read_sql_query(
    "SELECT (cast(GrossProfit AS SIGNED) - cast(Budget AS SIGNED )) AS Profit FROM movie WHERE Country='USA' AND ContentRating = 'NC-17' AND Budget IS NOT NULL AND GrossProfit IS NOT NULL ORDER BY Profit DESC",
    conn)

data = [data1["Profit"], data2["Profit"], data3["Profit"], data4["Profit"],
        data5["Profit"]]  # combine all these tables into one
labels = ["G", "PG", "PG-13", "R", "NC-17"]
fig = plt.figure(1, figsize=(9, 6))  # set up a box and whisker plot to show this data
ax = fig.add_subplot(111)
bp = ax.boxplot(data, labels=labels)  # create labels for the plot
plt.title("Gross Profitability of Content Ratings in the USA")
plt.xlabel("Content Rating")
plt.ylabel("Gross Profit")
plt.show()

for k, v in enumerate(labels):
    print("Mean for " + v + ": " + str(scipy.mean(data[k])))
    print("StdDev for " + v + ": " + str(scipy.std(data[k])))
