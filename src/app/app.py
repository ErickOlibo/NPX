"""This module is the REAL main application. Trying to create a more
readable code.
"""

import customtkinter
import os
from PIL import Image
from collections.abc import Callable
from helpers import View
from gui.login_view import LoginView
from gui.navigation_bar import NavigationBar


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


    def show_main_view(self):
        self.title("NPX App | Your Secret Companion")
        self.geometry(f"{self.main_view_size[0]}x{self.main_view_size[1]}")
        self.resizable(True, True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.navigation_bar = NavigationBar(self)
        self.navigation_bar.grid(row=0, column=0, sticky="nsew")
        self.navigation_bar.grid_rowconfigure(4, weight=1)
    
    
    def show_login_view(self):
        self.title("NPX App | Login Screen")
        self.geometry(f"{self.login_view_size[0]}x{self.login_view_size[1]}")
        self.resizable(False, False)

        self.login_view = LoginView(self, self._login_view_button_pressed)
        self.login_view.grid(row=0, column=0, padx=120, pady=85, sticky="ns")

    def _login_view_button_pressed(self):
        (user, password) = self.login_view.get_credentials()
        print(f"CRED: {user} | {password}")
        self.login_view.grid_forget()
        self.show_main_view()


if __name__ == "__main__":
    app = App()
    app.mainloop()