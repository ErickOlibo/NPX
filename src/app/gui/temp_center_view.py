import customtkinter
import os
from collections.abc import Callable
from PIL import Image

class TempCenterView(customtkinter.CTkFrame):
    
    def __init__(self, master, title: str):
        super().__init__(master)
        
        # self.center_view = customtkinter.CTkFrame(
        #     self, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.button = customtkinter.CTkButton(
            self, text=title, compound="left")
        self.button.grid(row=0, column=0, padx=20, pady=300)

    # def get_view(self) -> customtkinter.CTkFrame:
    #     return 