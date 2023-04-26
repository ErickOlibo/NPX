"""This module creates a login view."""
from collections.abc import Callable
import customtkinter
from helpers import Assets, CustomImage, SessionData, StartUp


class LoginView(customtkinter.CTkFrame):
    """A view of type CTkFrame to embeded in custom GUI design."""
    def __init__(self, master, action: Callable[[], SessionData]):
        """Instantiate with the necessary attributes

        Parameters
        ----------
            master: Any
                The object that will be owning this object.
            action: Callable
                a method to trigger in the master when the button is pressed
        """
        super().__init__(master)
        self._action = action
        self._attach_logo_to_login_view()
        self._attach_title_credentials()
        self._attach_login_signin_v2()
        self._attach_message_box()

    # def get_credentials(self) -> tuple[str, str]:
    #     """Get the values for the username and the password that were entered.

    #     Returns
    #     -------
    #         tuple[str, str]: plaintext username and password
    #     """
    #     return (self._username.get(), self._password.get())
    
    def set_wrong_credentials_message(self, message: str):
        self._message_box.configure(text=f"* {message}")
        pass

    def _attach_logo_to_login_view(self):
        logo_image = CustomImage((45, 45), Assets.NPX_LOGO).image
        label = customtkinter.CTkLabel(
            self, text="     NPX App", image=logo_image,
            compound="left", font=customtkinter.CTkFont(size=25, weight="bold"))
        label.grid(row=0, column=0, padx=30, pady=(10, 15))

    def _attach_title_credentials(self):
        login_label = customtkinter.CTkLabel(
            self, text="My Secret Journal",
            font=customtkinter.CTkFont(size=20, weight="bold"))

        login_label.grid(row=2, column=0, padx=30, pady=(50, 15))
        self._username = customtkinter.CTkEntry(
            self, width=200, placeholder_text="username")
        self._username.grid(row=3, column=0, padx=30, pady=(15, 15))
        self._password = customtkinter.CTkEntry(
            self, width=200, show="*", placeholder_text="password")
        self._password.grid(row=4, column=0, padx=30, pady=(0, 15))

    def _attach_login_signin_v2(self):
        self._frame = customtkinter.CTkFrame(self)
        self._frame.configure(fg_color="transparent")
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=1)

        self._login_button = customtkinter.CTkButton(
            self._frame, text="Login", command=self._login_button_pressed,
            width=80, font=customtkinter.CTkFont(weight="bold"))

        self._signin_button = customtkinter.CTkButton(
            self._frame, text="Sign in", command=self._signin_button_pressed,
            width=80, font=customtkinter.CTkFont(weight="bold"))

        self._signin_button.grid(row=0, column=0, padx=(0, 20), pady=(0, 0), sticky="w")
        self._login_button.grid(row=0, column=1, padx=(20, 0), pady=(0, 0), sticky="e")

        self._frame.grid(row=5, column=0, padx=30, pady=(15, 15))

    def _attach_message_box(self):
        self._message_box = customtkinter.CTkLabel(
            self, text="",
            font=customtkinter.CTkFont(size=15, weight="normal"),
            text_color="red", justify="left")
        self._message_box.grid(row=6, column=0, padx=30, pady=(10, 15), sticky="w")

    def _login_button_pressed(self):
        data = SessionData(self._username.get(), self._password.get(), StartUp.LOG_IN)
        self._action(data)

    def _signin_button_pressed(self):
        data = SessionData(self._username.get(), self._password.get(), StartUp.SIGN_IN)
        self._action(data)
