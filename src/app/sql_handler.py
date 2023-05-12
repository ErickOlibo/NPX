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

    def get_data_desc(self, username: str):
        """Return all entries in the entries table sorted by user, and date and time in descending order

         Parameters
        ----------
            username: str
                The username entered in the field

        Returns
        -------
            A list with userdata"""
        sql = f"SELECT id, title, text, date, time, tags " \
              f"FROM {SQLTable.ENTRIES} " \
              f"WHERE user = ? " \
              f"ORDER BY date DESC, time DESC " \
              f"LIMIT 5"
        user = username
        self._cursor.execute(sql, (user,))
        userdata = self._cursor.fetchall()
        data_of_user = []
        if not userdata:
            # Return an empty list or a message indicating no entries were found
            return []
        for i, entry in enumerate(userdata):
            try:
                id = entry[0]
            except IndexError:
                id = ""
            try:
                title = entry[1]
            except IndexError:
                title = ""
            try:
                text = entry[2]
            except IndexError:
                text = ""
            try:
                date = entry[3]
            except IndexError:
                date = ""
            try:
                tags = entry[5]
            except IndexError:
                tags = ""
            data_of_user.append({
                'id': id,
                'title': title,
                'first_sentence': text,
                'date': date,
                'tag': tags,
            })
        return data_of_user

    '''get_data_on_click was for call from _journal_entry_get_content or on_click'''
    # def get_data_on_click(self, id: int):
    #     """show content in the main window when clicking quick access entry
    #
    #              Parameters
    #             ----------
    #                 username: str
    #                     The username entered in the field
    #
    #             Returns
    #             -------
    #                 """
    #     sql = f"SELECT title, text, tags " \
    #           f"FROM {SQLTable.ENTRIES} " \
    #           f"WHERE id = ? "
    #     self._cursor.execute(sql, (id,))
    #     title, text, tags = self._cursor.fetchone()
    #     print(title,text,tags)
    #     return title, text, tags

    def row_count_entries_table(self) -> int:
        sql = f"SELECT COUNT(*) FROM {SQLTable.ENTRIES}"
        return self._cursor.execute(sql).fetchone()[0]

    def close_connection(self):
        """Close the SQLite connection after use"""
        self._conn.close()
