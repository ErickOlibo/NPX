"""This module is a collection of constan and enums needed."""
import os
from enum import Enum, auto
from collections.abc import Callable
import customtkinter
from PIL import Image


class ExtendEnum(Enum):
    """
    Create the list of enums by value or name depending on type.
    Inspired by @Jeff https://stackoverflow.com/a/54919285/8699673
    """
    @classmethod
    def list(cls, list_type):
        """Return the list of all Enum cases as specified type."""

        if list_type == "name":
            enum_list = list(map(lambda c: c.name, cls))
        if list_type == "value":
            enum_list = list(map(lambda c: c.value, cls))
        return enum_list


class SQLTable(Enum):
    """Enum listing the database table names."""
    USERDATA = auto()
    ENTRIES = auto()

    def __str__(self):
        return str(self.name.lower())


class SQLCreateTable(Enum):
    """Enum listing the CREATE TABLE statements used in this App."""
    USERDATA = """
        CREATE TABLE IF NOT EXISTS userdata(
        id INTEGER PRIMARY KEY,
        username VARCHARD(255) NOT NULL,
        password VARCHARD(255) NOT NULL,
        UNIQUE(username)
        )
    """
    ENTRIES = """To Fill In Later"""

    def __str__(self):
        return str(self.value)


class StartUp(Enum):
    """Enum listing the option available at the start of the NPX app"""
    SIGN_IN = auto()
    LOG_IN = auto()


class View(Enum):
    """Enum listing the name of the different views in the NPX app."""

    JOURNAL = auto()
    PLANNING = auto()
    CHALLENGES = auto()
    LOGIN = auto()
    LOGOUT = auto()
    NAVIGATION_BAR = auto()


class Assets(ExtendEnum):
    """Enum listing different name of assets in the icon folder"""
    DARK_JOURNAL = auto()
    LIGHT_JOURNAL = auto()
    DARK_PLANNING = auto()
    LIGHT_PLANNING = auto()
    DARK_CHALLENGES = auto()
    LIGHT_CHALLENGES = auto()
    DARK_LOGIN = auto()
    LIGHT_LOGIN = auto()
    DARK_LOGOUT = auto()
    LIGHT_LOGOUT = auto()
    NPX_LOGO = auto()

    def __str__(self):
        asset_path = f"gui/assets/icons/{self.name.lower()}.png"
        return os.path.join(
            os.path.dirname(os.path.realpath(__file__)), asset_path)


class SessionIssue(Enum):
    """Enum listing the different issues that can occur during startup"""
    USERNAME_TAKEN = "Username Already Taken!"
    WRONG_USERNAME = "Wrong Username!"
    WRONG_PASSWORD = "Wrong Password!"
    EMPTY_USERNAME = "Username Field is Empty!"
    EMPTY_PASSWORD = "Password Field is Empty!"
    UNKNOWN = "Unknown Issue!"
    NONE = "None"

    def __str__(self):
        return str(self.value)


class CustomImage():
    """A image of type customtkinter.CTkImage to add to a custom frame"""
    def __init__(self, size: tuple[int, int], light: Assets = None, dark: Assets = None):
        """Instantiate with the necessary attributes

        Parameters
        ----------
            size: tuple[int, int]
                The width and height of the returned image
            light: Assets, optional
                The path to the file to use as default image, or as image for
                the dark mode. Defaults to None.
            dark: Assets, optional
                The path to the file to use as image for the light mode.
                Defaults to None.
        """
        self._size = size
        if None in [light, dark]:
            image = Image.open(str(light))
            self._image = customtkinter.CTkImage(image, size=size)
        else:
            light_image = Image.open(str(dark))  # image for light background
            dark_image = Image.open(str(light))  # image for dark background
            self._image = customtkinter.CTkImage(light_image, dark_image)

    @property
    def image(self) -> customtkinter.CTkImage:
        """
        Get the image resulting from the parameters entered.

        Returns
        -------
            customtkinter.CTkImage: The image requested as instance of.
        """
        return self._image


class CustomTabButton():
    """A button of type custom.CTkButton to use as a tab bar button"""
    def __init__(self, master, title: str, icon: customtkinter.CTkImage,
                 action: Callable[[], None], position: tuple[int, int], stick: str):
        """Instantiate with the necessary attributes

        Parameters
        ----------
            master: Any
                The object that will be owning this object.
            title: str
                The label text of the button.
            icon: customtkinter.CTkImage
                The icon to be place at the left of the label.
            action: Callable
                a method to trigger in the master when the button is pressed
            position: tuple[int, int]
                The grid position this element has in the master's grid
        """
        self._btn = customtkinter.CTkButton(
            master, corner_radius=0, height=40, border_spacing=20,
            text=f"{title}", fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), image=icon, anchor="w",
            font=customtkinter.CTkFont(size=15), command=action)
        self._btn.grid(row=position[0], column=position[1], sticky=stick)

    @property
    def button(self) -> customtkinter.CTkButton:
        """
        Get the button resulting from the parameters entered.

        Returns
        -------
            customtkinter.CTkButton: The button requested as instance of.
        """
        return self._btn


class SessionData():
    """A container for the credential and the type of startup."""
    def __init__(self, username: str, password: str, type: StartUp):
        """Instantiate with the necessary attributes.

        Parameters
        ----------
            name: str
                The username entered during this login/sign in session
            password: str
                The password entered duing this login/sing in session
            type: StartUp
                The type, Login or Sign in of the current startup session
        """
        self._username = username
        self._password = password
        self._type = type

    @property
    def cookie(self) -> tuple[str, str, StartUp]:
        """
        Get the username, password and startup type of the current session.

        Returns:
            tuple[str, str, StartUp]: respectivelly, username, password, type.
        """
        return (self._username, self._password, self._type)

    @property
    def username(self) -> str:
        """
        Return the username of the current session.

        Returns:
        - str: the username entered.
        """
        return self._username

    @property
    def password(self) -> str:
        """
        Return the password of the current session.

        Returns:
        - str: the password entered.
        """
        return self._password

    @property
    def type(self) -> StartUp:
        """
        Return the Startup type (Login or Sign in) of the current session.

        Returns:
        - StartUp: the type choosen.
        """
        return self._type

    def __str__(self) -> str:
        return f"User: {self._username}\nPass: {self._password}\nType: {self._type.name}"


SAMPLE_ENTRIES = {
    0: ["Sat 8 April", "A Sunny Day", ("Stress", "Anger"),
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..."],
    1: ["Wed 5 April", "Waiting for the Results", ("Anxiety", "Panic", "Not eating"),
        "Ut etiam sit amet nisl purus in mollis. \
            Donec massa sapien faucibus et molestie ac feugiat..."],
    2: ["Mon 27 March", "Not Sure How I Feel", (),
        "Sed augue lacus viverra vitae congue eu consequat. \
            Lacinia quis vel eros donec ac. At quis risus sed vulputate odio ut enim...."],
}
