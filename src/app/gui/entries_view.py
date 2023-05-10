import customtkinter
from sql_handler import SQLHandler
from helpers import EntriesData


class EntriesView(customtkinter.CTkFrame):

    def __init__(self, master: customtkinter.CTk, username: str):
        super().__init__(master)
        self._master = master
        self._username = username
        self._handler = SQLHandler()
        self.configure(fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # set the UI elements
        self._search_bar()
        self._result_view()

    
    def _search_bar(self):
        self._search_entry = customtkinter.CTkEntry(self, placeholder_text="Search")
        self._search_entry.grid(row=0, column=0, padx=20, pady=20, sticky="new")
    
    def _result_view(self):
        entries = self._handler.select_all_entries_for_user(self._username)
        size = len(entries)
        
        self._scroll_view = ResultScrollView(self)
        self._scroll_view.set_entries(entries)
        self._scroll_view.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="sew")
        pass
    
    def _all_entries(self):
        entries = self._handler.select_all_entries_for_user(self._username)



class ResultScrollView(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, label_text="Scroll View", height=450)
        self._master = master
        self.grid_columnconfigure(0, weight=1)
        
    
    def set_entries(self, entries: dict[int, EntriesData]):
        for i, value in enumerate(entries.values()):
            checkbox = customtkinter.CTkCheckBox(self, text=value.title)
            checkbox.grid(row=i, column=0, padx=20, pady=(20, 0), sticky="w")
            # print(f"{i} - {value.title}")
            
    
    def set_scroll_title(self, title: str):
        
        pass