import customtkinter
from sql_handler import SQLHandler


class EntriesView(customtkinter.CTkFrame):

    def __init__(self, master: customtkinter.CTk):
        super().__init__(master)
        self._master = master
        self._handler = SQLHandler()
        self.configure(fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)


        # set the UI elements
        self._search_bar()
        self._result_view()
        self._all_entries()

    
    def _search_bar(self):
        self._search_entry = customtkinter.CTkEntry(self, placeholder_text="Search")
        self._search_entry.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
    
    def _result_view(self):
        size = self._handler.row_count_entries_table()
        
        self._scroll_view = ResultScrollView(self, f"{size} Entries in Total")
        pass
    
    def _all_entries(self):
        self._handler.select_all_entries()



class ResultScrollView(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)