import sqlite3
import hashlib
from sqlite3 import Connection, Error
from helpers import SQLCreateTable, SQLTable

class SQLHandler:
    """This handles every query to the database. """

    def __init__(self):
        database_path = "db/npx_app.db"
        self._conn = self._create_connection(database_path)
        self._cursor = self._conn.cursor()
        self._create_userdata_table()


    def _create_connection(self, path: str) -> Connection:
        try:
            conn = sqlite3.connect(path)
        except Error as err:
            print(f"Connection to the database failed. {err=}, {type(err)=}")
        else:
            return conn
    
    def _create_userdata_table(self):
        sql = str(SQLCreateTable.USERDATA)
        self.create_table(sql)
    
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
        if all(item in ["username", "password"] for item in kwargs.keys()):
            sql = f"INSERT OR IGNORE INTO {table} (username, password) VALUES (?, ?)"
            hash_password = self._get_hash_digest(kwargs["password"])
            self._cursor.execute(sql, (kwargs["username"], hash_password))
            self._conn.commit()

    
    def _get_hash_digest(self, password: str ) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

handler = SQLHandler()
handler.insert_into(SQLTable.USERDATA, username="Eri", password="22OLIBO")
