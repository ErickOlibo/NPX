"""This module create an instance of a SQLLite handler."""
import os
import sqlite3
import hashlib
from sqlite3 import Connection, Error
from helpers import SQLCreateTable, SQLTable, SessionData, EntriesData


class SQLHandler:
    """This handles every query to the database. """

    def __init__(self):
        db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "db/npx_app.db")
        self._conn = self._create_connection(db_path)
        self._cursor = self._conn.cursor()
        self._create_userdata_table()
        self._create_entry_table()

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

    def _create_entry_table(self):
        sql = str(SQLCreateTable.ENTRIES)
        self.create_table(sql)

    def create_table(self, sql: str):
        """Create a table from the sql statement.

        Parameters
        ----------
            sql: str
                a CREATE TABLE statement to execute
        """
        try:
            self._cursor.execute(sql)
        except Error as err:
            print(f"Failed to execute SQL CREATE TABLE statement. {err=}, {type(err)=}")

    def insert_into_userdata(self, data: SessionData):
        """Insert into table named userdata the session's username and password.

        Parameters
        ---------
            data: SessionData)
                Contain the session username, password and type of startup
        """
        sql = f"INSERT OR IGNORE INTO {SQLTable.USERDATA} (username, password) VALUES (?, ?)"
        username = data.username.lower()
        password = self._get_hash_digest(data.password)
        self._cursor.execute(sql, (username, password))
        self._conn.commit()

    def insert_into_entries(self, data: EntriesData):
        """Insert a new entry into the table named entries.

        Parameters
        ----------
            data: EntriesData
                The username, the journal entry, the date, the time, and the tags
                to insert into the database.
        """
        sql = f"INSERT INTO {SQLTable.ENTRIES} (user, title, text, date, time, tags) VALUES (?, ?, ?, ?, ?, ?)"
        self._cursor.execute(sql, (data.user, data.title, data.text, data.datenow, data.timenow, data.tags))
        self._conn.commit()

    def _get_hash_digest(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def verified_user(self, username: str, password: str) -> bool:
        """Verify if the credential for a loging in users is correct.

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

    def row_count_entries_table(self) -> int:
        """Returns the number of rows in the Entries table"""
        sql = f"SELECT COUNT(*) FROM {SQLTable.ENTRIES}"
        return self._cursor.execute(sql).fetchone()[0]

    def select_all_entries_for_user(self, user: str) -> dict[int, EntriesData]:
        """Returns the list of entries made by a user in the Entries table.

        Parameters
        ----------
            user: str
                The user for which the entries are fetched

        Returns
        -------
            dict[int, EntriesData]: The entries data in a dictionary with IDs as keys
        """
        print(f"[select_all_entries_for_user] --> {user}")
        sql = f"SELECT * FROM {SQLTable.ENTRIES} WHERE user = ? ORDER BY date DESC, time DESC"
        self._cursor.execute(sql, (user.lower(),))
        rows = self._cursor.fetchall()
        results = {
            str(row[0]): EntriesData(row[1], row[2], row[3], row[4], row[5], row[6])
            for row in rows}
        return results

    def select_entries_for_search_text(self, user: str, text: str) -> dict[int, EntriesData]:
        """selects from the entries table the instance satisfying the search query

        Parameters
        ----------
            user: str
                The user for which the entries are fetched
            text: str
                The search text to lookup

        Returns
        -------
            dict[int, EntriesData]:
                returns the data fetched as a dictionary [ID : EntriesData]
        """
        like_text = f"%{text}%"
        select = f"SELECT * FROM {SQLTable.ENTRIES}"
        where = "WHERE user = ? AND title LIKE ?"
        order = "ORDER BY date DESC, time DESC"
        sql = f"{select} {where} {order}"

        self._cursor.execute(sql, (user.lower(), like_text.lower()))
        rows = self._cursor.fetchall()
        results = {
            str(row[0]): EntriesData(row[1], row[2], row[3], row[4], row[5], row[6])
            for row in rows}
        return results

    def close_connection(self):
        """Close the SQLite connection after use"""
        self._conn.close()
