import sqlite3
import customtkinter


class Buttons(sqlite3,customtkinter):
    
    def __init__(self,root):
        self._root = root
        self._add_button = customtkinter.CTkButton(root, text='Add entry',
                                                   command= self.add_entry,
                                                   hover= True)
        self._delete_button = customtkinter.CTkButton(root, text='Delete entry',
                                                      command= self.delete_entry,
                                                      state= 'disabled')
        self._conn = sqlite3.Connection('user.db')
        self._cursor = self._conn.cursor()
    
    def add_entry(self, root):
        self._root = root
        self._cursor.execute("""
        CREATE TABLE IF NOT EXISTS journal(
        title NOT NULL VARCHAR(255) PRIMARY KEY,
        entry VARCHAR(max)
        )
        """)
        title = ''
        entry = ''
        self._cursor.execute("INSERT INTO journal (title, entry)"
                             "VALUES (?, ?)", (title, entry))
        self._conn.commit()

        self._delete_button = customtkinter.CTkButton(root, text='Delete entry',
                                                      command= self.delete_entry;
                                                      hover= True)


    def delete_entry():
        pass