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
        self._edit_button = customtkinter.CTkButton(root, text='Edit',
                                                    command= self.edit_entry,
                                                    state= 'disabled')
        self._clear_button = customtkinter.CTkButton(root, text='Clear',
                                                    command= self.clear_entry,
                                                    state= 'disabled')
        self._conn = sqlite3.Connection('user.db')
        self._cursor = self._conn.cursor()
    
    def add_entry(self, root, title, entry):
        self._root = root
        self._cursor.execute("""
        CREATE TABLE IF NOT EXISTS journal(
        title NOT NULL VARCHAR(255) PRIMARY KEY,
        entry VARCHAR(max)
        )
        """)
        self._cursor.execute("INSERT INTO journal (title, entry)"
                             "VALUES (?, ?)", (title, entry))
        self._conn.commit()

        self._delete_button = customtkinter.CTkButton(root, text='Delete entry',
                                                      command= self.delete_entry,
                                                      hover= True)
        self._edit_button = self._edit_button = customtkinter.CTkButton(root, text='Edit',
                                                    command= self.edit_entry,
                                                    hover= True)
        self._clear_button = customtkinter.CTkButton(root, text='Clear',
                                                    command= self.clear_entry,
                                                    hover= True)


    def delete_entry():
        pass

    
    def edit_entry():
        pass


    def clear_entry(self, text):
        pass