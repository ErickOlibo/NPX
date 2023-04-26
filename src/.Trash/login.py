"""This module create an instance of the Desktop login view"""
import customtkinter
import os
from PIL import Image
from collections.abc import Callable

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class LoginView(customtkinter.CTk):
    """Instantiate the Login view with its characteristics"""

    width = 500
    height = 500

    def __init__(self):
        super().__init__()

        self.title("NPX App | Login Page")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        
        self.assets_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "assets")

        # create login frame
        self.login_view = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_view.grid(row=0, column=0, padx=120, pady=85, sticky="ns")
        
        self.logo_image = customtkinter.CTkImage(
            self._getImage("npx_logo.png"), size=(45, 45))
        self.logo_label = customtkinter.CTkLabel(
            self.login_view, text="     NPX App", image=self.logo_image,
            compound="left", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=30, pady=(10, 15))
        
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
            self.login_view, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=5, column=0, padx=30, pady=(15, 15))

        # # create main frame
        # self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        # self.main_frame.grid_columnconfigure(0, weight=1)
        # self.main_label = customtkinter.CTkLabel(self.main_frame, text="CustomTkinter\nMain Page",
        #                                          font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        # self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        # self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

    def login_event(self):
        print("Login pressed - username:", self.username.get(), "password:", self.password.get())
        print(f"Login -> username: {self.username.get()} | password: {self.password.get()}")

        #self.login_view.grid_forget()  # remove login frame
        #self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

    # def back_event(self):
    #     #self.main_frame.grid_forget()  # remove main frame
    #     self.login_view.grid(row=0, column=0, sticky="ns")  # show login frame
    
    def _set_top_logo(self):
        logo_image = customtkinter.CTkImage(
            self._getImage("npx_logo.png"), size=(35, 35))
        top_logo = customtkinter.CTkLabel(
            self.login_view, text="     NPX App", image=logo_image,
            compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        top_logo.grid(row=0, column=0, padx=20, pady=20)
        return top_logo
    
    def _getImage(self, path: str)-> Image:
        return Image.open(os.path.join(self.assets_path, path))
    


if __name__ == "__main__":
    app = LoginView()
    app.mainloop()