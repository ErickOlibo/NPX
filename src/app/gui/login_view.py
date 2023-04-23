import customtkinter
import os
from collections.abc import Callable
from PIL import Image

class LoginView(customtkinter.CTkFrame):
    assets_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "assets")
    def __init__(self, master, action: Callable[[], None]):
        super().__init__(master)

        self._attach_logo_to_login_view()
        self._attach_title_credentials()
        self.login_button = customtkinter.CTkButton(
            self, text="Login", command=action, width=200)
        self.login_button.grid(row=5, column=0, padx=30, pady=(15, 15))

    def get_credentials(self) -> tuple[str, str]:
        """Get the values for the username and the password that were entered.

        Returns
        -------
            tuple[str, str]: plaintext uusername and password
        """
        return (self.username.get(), self.password.get())

    def _attach_logo_to_login_view(self):
        self.logo_image = customtkinter.CTkImage(
            self._getImage("npx_logo.png"), size=(45, 45))
        self.logo_label = customtkinter.CTkLabel(
            self, text="     NPX App", image=self.logo_image,
            compound="left", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=30, pady=(10, 15))

    def _attach_title_credentials(self):
        self.login_label = customtkinter.CTkLabel(
            self, text="Sign in / Login",
            font=customtkinter.CTkFont(size=20, weight="bold"))

        self.login_label.grid(row=2, column=0, padx=30, pady=(50, 15))
        self.username = customtkinter.CTkEntry(
            self, width=200, placeholder_text="username")
        self.username.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.password = customtkinter.CTkEntry(
            self, width=200, show="*", placeholder_text="password")
        self.password.grid(row=4, column=0, padx=30, pady=(0, 15))

    def _getImage(self, path: str)-> Image:
        return Image.open(os.path.join(self.assets_path, path))

