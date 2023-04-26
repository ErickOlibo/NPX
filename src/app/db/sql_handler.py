import sqlite3
from sqlite3 import Connection, Error
from helpers import SQLCreateTable, SQLTable

class SQLHandler:
    """This handles every query to the database. """
    
    def __init__(self):
        database_path = "npx_app.db"
        self._conn = self._create_connection(database_path)
        self._cursor = self._conn.cursor()
        
        

    
    def _create_connection(self, path: str) -> Connection:
        try:
            conn = sqlite3.connect(path)
        except Error as err:
            print(f"Connection to the database failed. {err=}, {type(err)=}")
        else:
            return conn
    
    def create_table(self, sql: str):
        """Create a table from the sql statement

        Parameters
        ----------
            sql: str
                a CREATE TABLE statement to execute
        """
        try:
            self._cursor.execute(sql)
        except Error as err:
            print(f"Failed to execute SQL CREATE TABLE statement. {err=}, {type(err)=}")
    
    def insert_into(self, table: SQLTable, **kwargs):
        if ["username", "password"] in kwargs.keys():
            print("valid")
        else:
            print("Not Valid")
        pass

handler = SQLHandler()
handler.insert_into(SQLTable.USERDATA, username="Erick", password="OLIBO")