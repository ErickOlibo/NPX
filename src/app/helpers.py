"""This module is a collection of constan and enums needed."""
import os
from enum import Enum, auto
import customtkinter
from PIL import Image
from collections.abc import Callable

class View(Enum):
    """Enum listing the name of the different views in the NPX app."""

    JOURNAL = auto()
    PLANNING = auto()
    CHALLENGES = auto()
    LOGIN = auto()
    LOGOUT = auto()
    NAVIGATION_BAR = auto()


class Assets(Enum):
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
            self._CTk = customtkinter.CTkImage(image, size=size)
        else:
            light_image = Image.open(str(dark)) # image for light background
            dark_image = Image.open(str(light)) # image for dark background
            self._CTk = customtkinter.CTkImage(light_image, dark_image)

    @property
    def image(self) -> customtkinter.CTkImage:
        """
        Get the image resulting from the parameters entered.

        Returns
        -------
            customtkinter.CTkImage: The image requested as instance of.
        """
        return self._CTk

class CustomTabButton():
    """A button of type custom.CTkButton to use as a tab bar button"""
    def __init__(self, master,  title: str,
                               icon: customtkinter.CTkImage,
                               action: Callable[[], None],
                               position: tuple[int, int],
                               stick: str):
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


SAMPLE_ENTRIES = {
    0: ["Sat 8 April", "A Sunny Day", ("Stress", "Anger"),
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..."],
    1: ["Wed 5 April", "Waiting for the Results", ("Anxiety", "Panic", "Not eating"),
        "Ut etiam sit amet nisl purus in mollis. Donec massa sapien faucibus et molestie ac feugiat..."],
    2: ["Mon 27 March", "Not Sure How I Feel", (),
        "Sed augue lacus viverra vitae congue eu consequat. Lacinia quis vel eros donec ac. At quis risus sed vulputate odio ut enim...."],
}