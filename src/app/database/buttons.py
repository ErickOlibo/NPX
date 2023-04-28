import sqlite3
import customtkinter


class Buttons(sqlite3,customtkinter):
    
    def __init__(self,root):
        self._root = root
        self._add_button = customtkinter.CTkButton(root, text='Add entry', command= self.add_entry)
        self._delete_button = customtkinter.CTkButton(root, text='Delete entry', command= self.delete_entry)
    
    def add_entry():
        pass

    def delete_entry():
        pass