from sqlalchemy import create_engine
import pandas
import numpy
import matplotlib.pyplot as plt
#Question 5: Over​ ​time,​ ​how​ ​has​ ​interest​ ​in​ ​specific​ ​genres​ ​changed​ ​for​ ​different​ ​regions​ ​around​ ​the world?​ ​What​ ​are​ ​the​ ​most​ ​popular​ ​genres​ ​now?​
#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')#create connection to our movie database
conn = engine.connect()
conn.begin()
data = pandas.read_sql_query("", conn)
print(data)