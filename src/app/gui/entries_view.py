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
        content = self._search_var.get()
        print(f"Text To Search: {content}")
        result = self._handler.select_entries_for_search_text(self._username, content)
        print(f"Text [{content}] Returns {len(result)} Entries")
        self._scroll_view.set_entries(result)



class ResultScrollView(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, label_text="Results", height=450)
        self._master = master
        self.rows = []
        self.grid_columnconfigure(0, weight=1)
        
    
    def set_entries(self, entries: dict[int, EntriesData]):
        self.remove_rows()
        print(f"Size Entries: {len(entries)}")
        self.set_title(f"Result: {len(entries)} Entries")
        for i, value in enumerate(entries.values()):
            row = TableRow(self, value.title)
            row.configure(fg_color=("gray80", "gray20") if i % 2 == 0 else ("gray75", "gray15"))
            row.grid(row=i, column=0, sticky="ew")
            self.rows.append(row)

    def remove_rows(self):
        for row in self.rows:
            row.destroy()
        self.rows = []

    def set_title(self, title: str):
        print(f"New Title: {title}")
        # label = "Result"
        # if not title:

        self.configure(label_text=str(title))
        pass

class TableRow(customtkinter.CTkFrame):
    
    def __init__(self, master, title: str):
        super().__init__(master)
        self.configure(corner_radius=0)
        checkbox = customtkinter.CTkCheckBox(self, text=title)
        checkbox.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="w")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=0)
        # self.grid_columnconfigure((2,9), weight=1)
        # self.edit_button()
        # self.delete_button()
        pass
    
    # def configure(self, fg_color):
    #     self.configure(fg_color=fg_color)
        
    def edit_button(self):
        pass
    
    def delete_button(self):
        pass