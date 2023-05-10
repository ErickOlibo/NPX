import tkinter as tk
from tkinter import ttk
import customtkinter
from sql_handler import SQLHandler
from helpers import EntriesData


class EntriesView(customtkinter.CTkFrame):

    def __init__(self, master: customtkinter.CTk, username: str):
        super().__init__(master)
        self._master = master
        self._username = username
        self._handler = SQLHandler()
        self._search_var = customtkinter.StringVar()
        self._search_var.trace('w', self.search_text_changed)
        self.configure(fg_color="transparent")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        

        # set the UI elements
        self._search_bar()
        self._result_view()


    def _search_bar(self):
        search_label = customtkinter.CTkLabel(self, text="Search:")
        search_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        search_entry = customtkinter.CTkEntry(self, textvariable=self._search_var)
        search_entry.grid(row=0, column=1, padx=(0,20), pady=20, sticky="new")


    def _result_view(self):
        entries = self._handler.select_all_entries_for_user(self._username)
        self._scroll_view = ResultScrollView(self)
        self._scroll_view.set_entries(entries)
        self._scroll_view.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="sew")

    def search_text_changed(self, *args):
        print("SEARCH TEXT HAS CHANGED")
        pass



class ResultScrollView(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, label_text="Results", height=450)
        self._master = master
        self.grid_columnconfigure(0, weight=1)
        
    
    def set_entries(self, entries: dict[int, EntriesData]):
        print(f"Size Entries: {len(entries)}")
        for i, value in enumerate(entries.values()):
            checkbox = customtkinter.CTkCheckBox(self, text=value.title)
            checkbox.grid(row=i, column=0, padx=20, pady=(20, 0), sticky="w")
            # print(f"{i} - {value.title}")
            
    
    def set_scroll_title(self, title: str):
        
        pass