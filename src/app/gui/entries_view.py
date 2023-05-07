import customtkinter

class EntriesView():
    
    def __init__(self, master: customtkinter.CTk):
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=0)
        
        pass