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
from gui.temp_center_view import TempCenterView


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
        
        self.navigation_bar = NavigationBar(
            self, self._nav_tab_journal,
            self._nav_tab_planning,
            self._nav_tab_challenges,
            self._logout_pressed)
        self.navigation_bar.grid(row=0, column=0, sticky="nsew")
        self.navigation_bar.grid_rowconfigure(4, weight=1)
        
        # Set opening current View
        self.set_current_view("Journal Center View")
        

        
    
    def set_current_view(self, title: str) -> customtkinter.CTkFrame:
        self.current_view = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color=("gray90", "gray15"))
        self.current_view.grid_columnconfigure(0, weight=1)
        button = customtkinter.CTkButton(
            self.current_view, text=title, compound="left")
        button.grid(row=0, column=0, padx=20, pady=300)
        self.current_view.grid(row=0, column=1, sticky="nsew")

    
    def show_login_view(self):
        self.title("NPX App | Login Screen")
        self.geometry(f"{self.login_view_size[0]}x{self.login_view_size[1]}")
        self.resizable(False, False)

        self.login_view = LoginView(self, self._login_view_button_pressed)
        self.login_view.grid(row=0, column=0, padx=120, pady=85, sticky="ns")

    def _set_current_tab(self):
        pass
    
    
    # Button Pressed
    def _login_view_button_pressed(self):
        (user, password) = self.login_view.get_credentials()
        print(f"CRED: {user} | {password}")
        self.login_view.grid_forget()
        self.show_main_view()
    
    def _nav_tab_journal(self):
        self.navigation_bar.set_active_button(View.JOURNAL)
        self.set_current_view("Journal Center View")
        print(f"JOURNAL: {View.JOURNAL.value}")
    
    def _nav_tab_planning(self):
        self.navigation_bar.set_active_button(View.PLANNING)
        self.set_current_view("Planning Center View")
        print(f"PLANNING: {View.PLANNING.value}")
    
    def _nav_tab_challenges(self):
        self.navigation_bar.set_active_button(View.CHALLENGES)
        self.set_current_view("Challenges Center View")
        print(f"CHALLENGES: {View.CHALLENGES.value}")
    
    def _logout_pressed(self):
        print("LOGOUT")
        



if __name__ == "__main__":
    app = App()
    app.mainloop()