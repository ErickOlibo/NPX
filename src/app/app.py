"""This module is the REAL main application. Trying to create a more
readable code.
"""

import customtkinter
import os
from PIL import Image
from collections.abc import Callable
from helpers import View
from gui.login_view import LoginView


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    login_view_size = (500, 500)
    main_view_size = (1080, 720)
    assets_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "gui/assets")
    
    def __init__(self) -> None:
        super().__init__()
        
        self.show_login_view()


    def show_login_view(self):
        self.title("NPX App | Login Screen")
        self.geometry(f"{self.login_view_size[0]}x{self.login_view_size[1]}")
        self.resizable(False, False)
        self.login_view = LoginView(self)
        self.login_view.grid(row=0, column=0, padx=120, pady=85, sticky="ns")
        

    def _login_view_button_pressed(self):
        print("From the Login View")


if __name__ == "__main__":
    app = App()
    app.mainloop()