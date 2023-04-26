"""This module create an instance of a SQLLite handler."""
import os
import sqlite3
import hashlib
from sqlite3 import Connection, Error
from helpers import SQLCreateTable, SQLTable


class SQLHandler:
    """This handles every query to the database. """

    def __init__(self):
        db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "db/npx_app.db")
        #  database_path = "db/npx_app.db"
        self._conn = self._create_connection(db_path)
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
        """Insert into a table the values.

        This method host the most common queries to insrt rapidly values in the database.
        To insert a username and password it is important to reference the arguments
        with the appropriate name
        example: insert_into(SQLTable.USERDATA, username="user", password="pwd" )

        Parameters
        ----------
            table: SQLTable
                A table name as definied in the Enum SQLTable
            **kwargs: Any
                additional argument prefixed but the argument name
        """
        if all(item in ["username", "password"] for item in kwargs.keys()):
            sql = f"INSERT OR IGNORE INTO {table} (username, password) VALUES (?, ?)"
            username = str(kwargs["username"]).lower()
            password = self._get_hash_digest(kwargs["password"])
            self._cursor.execute(sql, (username, password))
            self._conn.commit()

    def _get_hash_digest(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def verified_user(self, username: str, password: str) -> bool:
        """Verify if the credential for a loging in users is correct

        Parameters
        ----------
            username: str
                The username entered in the field
            password: str
                The password entered in the field

        Returns
        -------
            bool: A boolean value of True is the verification was approved.
        """
        user_name = username.lower()
        hashed_password = self._get_hash_digest(password)
        sql = f"SELECT username FROM {SQLTable.USERDATA} WHERE username = ? AND password = ?"
        self._cursor.execute(sql, (user_name, hashed_password))
        return self._cursor.fetchone() is not None

    def username_taken(self, username: str) -> bool:
        """Verifyif a username is already taken before sign in a new user with the same name

        Parameters
        ----------
            username: str
                The username entered in the field

        Returns
        -------
            bool: A boolean value of True is the username already exist in the database.
        """
        user_name = username.lower()
        sql = f"SELECT username FROM {SQLTable.USERDATA} WHERE username = ?"
        self._cursor.execute(sql, (user_name,))
        return self._cursor.fetchone() is not None

    def close_connection(self):
        """Close the SQLite connection after use"""
        self._conn.close()
