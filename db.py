from sqlalchemy.engine import create_engine
import pandas

class db:

    def __init__(self):
        self.engine = create_engine('mysql://root:blue@localhost:3306/imdb')  # create connection to our movie database
        self.conn = self.engine.connect()
        self.conn.begin()

    def query(self, query):
        return pandas.read_sql_query(query, self.conn)

    def table(self, table):
        return pandas.read_sql_table(table, self.conn)