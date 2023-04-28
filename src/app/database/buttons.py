import sqlite3
from tkinter import *


class Buttons(tkinter,sqlite3):
    
    def __init__(self,root):
        self._root = root
        self._add_button = Button(root, text='Add entry', command= self.add_entry)
        self._delete_button = Button(root, text='Delete entry', command= self.delete_entry)
    
    def add_entry():
        pass

    def delete_entry():
        pass