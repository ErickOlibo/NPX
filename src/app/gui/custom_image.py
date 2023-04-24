"""This class create custom CTkImage that has the caracteristics
of holding both Dark and Light image component"""

import customtkinter
from PIL import Image


class CustomImage(customtkinter.CTkImage):
    
    def __init__(self, light_path: str, dark_path: str, size: tuple[int, int]):
        super().__init__()
        self._light_image = Image.open(dark_path) # image for light background
        self._dark_image = Image.open(light_path) # image for dark background
        self._size = size
