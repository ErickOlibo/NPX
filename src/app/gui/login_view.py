"""This module creates a login view."""
import customtkinter
from collections.abc import Callable
from helpers import Assets, CustomImage

class LoginView(customtkinter.CTkFrame):
    """A view of type CTkFrame to embeded in custom GUI design."""
    def __init__(self, master, action: Callable[[], None]):
        """Instantiate with the necessary attributes
        
        Parameters
        ----------
            master: Any
                The object that will be owning this object.
            action: Callable
                a method to trigger in the master when the button is pressed
        """
        super().__init__(master)
        self._attach_logo_to_login_view()
        self._attach_title_credentials()
        self._login_button = customtkinter.CTkButton(
            self, text="Login", command=action, width=200)
        self._login_button.grid(row=5, column=0, padx=30, pady=(15, 15))

    def get_credentials(self) -> tuple[str, str]:
        """Get the values for the username and the password that were entered.

        Returns
        -------
            tuple[str, str]: plaintext username and password
        """
        return (self._username.get(), self._password.get())

    def _attach_logo_to_login_view(self):
        self._logo_image = CustomImage((45, 45),Assets.NPX_LOGO).image
        self._logo_label = customtkinter.CTkLabel(
            self, text="     NPX App", image=self._logo_image,
            compound="left", font=customtkinter.CTkFont(size=25, weight="bold"))
        self._logo_label.grid(row=0, column=0, padx=30, pady=(10, 15))

    def _attach_title_credentials(self):
        self._login_label = customtkinter.CTkLabel(
            self, text="Sign in / Login",
            font=customtkinter.CTkFont(size=20, weight="bold"))

        self._login_label.grid(row=2, column=0, padx=30, pady=(50, 15))
        self._username = customtkinter.CTkEntry(
            self, width=200, placeholder_text="username")
        self._username.grid(row=3, column=0, padx=30, pady=(15, 15))
        self._password = customtkinter.CTkEntry(
            self, width=200, show="*", placeholder_text="password")
        self._password.grid(row=4, column=0, padx=30, pady=(0, 15))