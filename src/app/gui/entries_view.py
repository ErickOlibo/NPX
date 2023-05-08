import customtkinter


class EntriesView(customtkinter.CTkFrame):

    def __init__(self, master: customtkinter.CTk):
        super().__init__(master)
        self.configure(
            corner_radius=0,
            fg_color=("gray90", "gray15"))

        self.grid_columnconfigure(0, weight=1)
        button = customtkinter.CTkButton(
            self, text="ENTRIES", compound="left")
        button.grid(row=0, column=0, padx=20, pady=300)
        self.grid(row=0, column=1, sticky="nsew")
