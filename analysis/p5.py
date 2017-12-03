from sqlalchemy import create_engine
import pandas
import numpy
import matplotlib.pyplot as plt

#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')
conn = engine.connect()
conn.begin()
data = pandas.read_sql_query("", conn)
print(data)