"""This module is a collection of constan and enums needed."""
import os
from enum import Enum, auto
import customtkinter
from PIL import Image
from collections.abc import Callable

class View(Enum):
    """Enum listing the name of the different views in the GUI"""
    
    JOURNAL = auto()
    PLANNING = auto()
    CHALLENGES = auto()
    LOGIN = auto()
    LOGOUT = auto()


class Assets(Enum):
    
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
    def __init__(self, size: tuple[int, int], light: Assets = None, dark: Assets = None):
        self._size = size
        if None in [light, dark]:
            image = Image.open(str(light))
            self.CTk = customtkinter.CTkImage(image, size=size)
        else:
            light_image = Image.open(str(dark)) # image for light background
            dark_image = Image.open(str(light)) # image for dark background
            self.CTk = customtkinter.CTkImage(light_image, dark_image)

class CustomButton():
    def __init__(self, master,  title: str,
                               icon: customtkinter.CTkImage,
                               action: Callable[[], None],
                               position: tuple[int, int],
                               stick: str):
        self.btn = customtkinter.CTkButton(
            master, corner_radius=0, height=40, border_spacing=20,
            text=f"{title}", fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), image=icon, anchor="w",
            font=customtkinter.CTkFont(size=15), command=action)
        self.btn.grid(row=position[0], column=position[1], sticky=stick)


SAMPLE_ENTRIES = {
    0: ["Sat 8 April", "A Sunny Day", ("Stress", "Anger"),
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..."],
    1: ["Wed 5 April", "Waiting for the Results", ("Anxiety", "Panic", "Not eating"),
        "Ut etiam sit amet nisl purus in mollis. Donec massa sapien faucibus et molestie ac feugiat..."],
    2: ["Mon 27 March", "Not Sure How I Feel", (),
        "Sed augue lacus viverra vitae congue eu consequat. Lacinia quis vel eros donec ac. At quis risus sed vulputate odio ut enim...."],
}