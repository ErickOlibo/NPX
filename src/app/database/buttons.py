import sqlite3
import customtkinter


class Buttons(sqlite3,customtkinter):
    
    def __init__(self,root):
        self._root = root
        self._add_button = customtkinter.CTkButton(root, text='Add entry',
                                                   command= self.add_entry)
        self._delete_button = customtkinter.CTkButton(root, text='Delete entry',
                                                      command= self.delete_entry)
        self._conn = sqlite3.Connection('user.db')
        self._cursor = self._conn.cursor()
    
    def add_entry(self):
        self._cursor.execute("""
        CREATE TABLE IF NOT EXISTS journal(
        title NOT NULL VARCHAR(255) PRIMARY KEY,
        entry VARCHAR(max)
        )
        """)
        

    def delete_entry():
        pass