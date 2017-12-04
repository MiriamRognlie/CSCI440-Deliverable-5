from sqlalchemy.engine import create_engine
import pandas


class db:
    def __init__(self):
        self.engine = create_engine('mysql://root:blue@localhost:3306/imdb')  # create connection to our movie database
        self.conn = self.engine.connect()
        self.conn.begin()

    def query(self, query):
        return pandas.read_sql_query(query, self.conn)#returns the results of the given query from the database

    def table(self, table):
        return pandas.read_sql_table(table, self.conn)#returns an unedited table from the database

    def disconnect(self):# close this connection to the database
        self.conn.close()
