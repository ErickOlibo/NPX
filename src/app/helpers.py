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
    ENTRIES = """
        CREATE TABLE IF NOT EXISTS entries(
        id INTEGER PRIMARY KEY,
        user VARCHAR(255),
        title VARCHAR(255),
        text VARCHAR(1000),
        date DATE,
        time TIME,
        tags VARCHAR(255)
        )
    """

    def __str__(self):
        return str(self.value)


class StartUp(Enum):
    """Enum listing the option available at the start of the USUKU app"""
    SIGN_IN = auto()
    LOG_IN = auto()


class JournalButton(Enum):
    """Enum listing the different custom button on the Journal View"""
    SAVE = auto()
    DELETE = auto()
    EDIT = auto()
    CLEAR = auto()

    def __str__(self):
        return str(self.name)


class ViewState(Enum):
    """Enum listing the different state views can take during execution."""
    JOURNAL_INSERT = auto()
    JOURNAL_UPDATE = auto()

    def __str__(self):
        return str(self.name)


class View(Enum):
    """Enum listing the name of the different views in the USUKU app."""

    JOURNAL = auto()
    ENTRIES = auto()
    DIARY = auto()
    LOGIN = auto()
    LOGOUT = auto()
    NAVIGATION_BAR = auto()


class Assets(ExtendEnum):
    """Enum listing different name of assets in the icon folder"""
    DARK_JOURNAL = auto()
    LIGHT_JOURNAL = auto()
    DARK_ENTRIES = auto()
    LIGHT_ENTRIES = auto()
    DARK_DIARY = auto()
    LIGHT_DIARY = auto()
    DARK_LOGIN = auto()
    LIGHT_LOGIN = auto()
    DARK_LOGOUT = auto()
    LIGHT_LOGOUT = auto()
    USUKU_LOGO = auto()

    def __str__(self):
        asset_path = f"gui/assets/icons/{self.name.lower()}.png"
        return os.path.join(
            os.path.dirname(os.path.realpath(__file__)), asset_path)


class IssueMessage(Enum):
    """Enum listing the different issues that can occur during startup"""
    USERNAME_TAKEN = "Username Already Taken!"
    WRONG_USERNAME = "Wrong Username!"
    WRONG_PASSWORD = "Wrong Password!"
    EMPTY_USERNAME = "Username Field is Empty!"
    EMPTY_PASSWORD = "Password Field is Empty!"
    SHORT_USERNAME = "Username is too short!\n min. 3 characters!"
    LONG_USERNAME = "Username is too long!\n max. 15 characters!"
    WEAK_PASSWORD = "The Password is too Short!\n8 charaters minimum!"
    MISSING_SPECIAL = "Password needs one special\ncharacter:'!@#$%^&*?'!"
    NO_LOWER_PASSWORD = "Password needs at least\none lowercase character!"
    NO_UPPER_PASSWORD = "Password needs at least\none uppercase character!"
    NO_DIGIT_PASSWORD = "Password needs at least\none number!"
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
            username: str
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


class EntriesData():
    """Container for the data to enter in the entries table"""
    def __init__(self, user: str, title: str, text: str, datenow: str, timenow: str, tags: str):
        """Instantiate with the necessary attributes.

        Parameters
        ----------
            user: str
                The username of the person writting the journal
            title:str
                The title entered
            text: str
                The text entered
            datenow: str
                Today date as YYYY/MM/DD format
            timenow: str
                The time at the time of saving (HH:MM:SS)
            tags: str
                The tags added to the entry
        """
        self._user = user
        self._title = title
        self._text = text
        self._tags = tags
        self._datenow = datenow
        self._timenow = timenow

    def __str__(self) -> str:
        part_one = f"USER: {self._user}\nTITLE: {self._title}\nTEXT: {self._text}\n"
        part_two = f"DAY: {self._datenow} | TIME: {self._timenow}\nTAGS: {self._tags}\n"
        return part_one + part_two

    @property
    def user(self) -> str:
        """Return the username of this current entries data"""
        return self._user

    @property
    def title(self) -> str:
        """Return the title of the entry for this current entries data"""
        return self._title

    @property
    def text(self) -> str:
        """Return the content of the entry for this current entries data"""
        return self._text

    @property
    def tags(self) -> str:
        """Return the tags of the entry for this current entries data"""
        return self._tags

    @property
    def datenow(self) -> str:
        """Return the day of creation of the entry for this current entries data"""
        return self._datenow

    @property
    def timenow(self) -> str:
        """Return the time of creation of the entry for this current entries data"""
        return self._timenow
