import customtkinter

class JournalView(customtkinter.CTkFrame):

    def __init__(self, master: customtkinter.CTk):
        super().__init__(master)
        
        self._master = master
        master.grid_columnconfigure(0, weight=0)
        master.grid_columnconfigure(1, weight=0)
        master.grid_columnconfigure(2, weight=0)
        master.grid_rowconfigure(0, weight=1)
        pass

    def _entry_title(self):
        pass

    def _entry_text_box(self):
        pass

    def _entry_tags(self):
        pass

    def _buttons(self):
        pass

    def forget_view(self):
        pass
    