import customtkinter

class EntriesView():
    
    def __init__(self, master: customtkinter.CTk):
        self._view = customtkinter.CTkFrame(
            master, corner_radius=0, fg_color=("gray90", "gray15"))
        self._view.grid_columnconfigure(0, weight=1)
        button = customtkinter.CTkButton(
            self._view, text="ENTRIES", compound="left")
        button.grid(row=0, column=0, padx=20, pady=300)
        self._view.grid(row=0, column=1, sticky="nsew")
