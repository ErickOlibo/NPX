"""This module is the main application. The implementation starts here
and all actions should be in sync with this class as it interact with
the user
"""

import customtkinter
import os
from PIL import Image
from collections.abc import Callable
from helpers import View


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class MainApp(customtkinter.CTk):
    login_view_size = (500, 500)
    main_view_size = (900, 600)
    
    def __init__(self) -> None:
        super().__init__()
        
        # Prepare Login View
        self.title("NPX App | Login Screen")
        self.geometry(f"{self.login_view_size[0]}x{self.login_view_size[0]}")
        self.resizable(False, False)
        
        # Path to assets folder
        self.assets_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "gui/assets")
        
        # Create Login View
        self.login_view = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_view.grid(row=0, column=0, padx=120, pady=85, sticky="ns")
        
        # Attach Logotype and Logomark to top of Login view
        self._attach_logo_to_login_view()
        
        self._attach_title_credentials()
        # self.logo_image = customtkinter.CTkImage(
        #     self._getImage("npx_logo.png"), size=(45, 45))
        # self.logo_label = customtkinter.CTkLabel(
        #     self.login_view, text="     NPX App", image=self.logo_image,
        #     compound="left", font=customtkinter.CTkFont(size=25, weight="bold"))
        # self.logo_label.grid(row=0, column=0, padx=30, pady=(10, 15))
        
        # self.login_label = customtkinter.CTkLabel(
        #     self.login_view, text="Sign in / Login",
        #     font=customtkinter.CTkFont(size=20, weight="bold"))
        
        
        # self.login_label.grid(row=2, column=0, padx=30, pady=(50, 15))
        # self.username = customtkinter.CTkEntry(
        #     self.login_view, width=200, placeholder_text="username")
        # self.username.grid(row=3, column=0, padx=30, pady=(15, 15))
        # self.password = customtkinter.CTkEntry(
        #     self.login_view, width=200, show="*", placeholder_text="password")
        # self.password.grid(row=4, column=0, padx=30, pady=(0, 15))
        # self.login_button = customtkinter.CTkButton(
        #     self.login_view, text="Login", command=self.login_event, width=200)
        # self.login_button.grid(row=5, column=0, padx=30, pady=(15, 15))
        
    
    # PUBLIC METHODS
    
    
    
    
    # PRIVATE METHODS
    def _login_event(self):
        print(f"Credential: {self.username.get()} | {self.password.get()}")
    
    def _attach_title_credentials(self):
        self.login_label = customtkinter.CTkLabel(
            self.login_view, text="Sign in / Login",
            font=customtkinter.CTkFont(size=20, weight="bold"))
        
        self.login_label.grid(row=2, column=0, padx=30, pady=(50, 15))
        self.username = customtkinter.CTkEntry(
            self.login_view, width=200, placeholder_text="username")
        self.username.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.password = customtkinter.CTkEntry(
            self.login_view, width=200, show="*", placeholder_text="password")
        self.password.grid(row=4, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(
            self.login_view, text="Login", command=self._login_event, width=200)
        self.login_button.grid(row=5, column=0, padx=30, pady=(15, 15))
    
    def _attach_logo_to_login_view(self):
        self.logo_image = customtkinter.CTkImage(
            self._getImage("npx_logo.png"), size=(45, 45))
        self.logo_label = customtkinter.CTkLabel(
            self.login_view, text="     NPX App", image=self.logo_image,
            compound="left", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=30, pady=(10, 15))
    
    def _getImage(self, path: str)-> Image:
        return Image.open(os.path.join(self.assets_path, path))







if __name__ == "__main__":
    app = MainApp()
    app.mainloop()