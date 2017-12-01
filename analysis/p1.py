from sqlalchemy import create_engine
import pandas
import numpy

#Create the MySQL Engine
engine = create_engine('mysql://root:blue@localhost:3306/imdb')
conn = engine.connect()
conn.begin()
data = pandas.read_sql_query('select Country, count(*) as count from movie group by Country order by count desc;', conn)
print(data)