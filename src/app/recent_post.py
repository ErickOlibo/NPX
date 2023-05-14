"""This module creates a composite frame to display a post row"""
from datetime import datetime
import textwrap
from collections.abc import Callable
import customtkinter
from helpers import EntriesData
from sql_handler import SQLHandler


class RecentPostRow(customtkinter.CTkFrame):
    """A custom row holding a date frame and title frame"""
    def __init__(self, master, id: int, entry: EntriesData, action: Callable[[], int]):
        """Create a customtkinter frame with the proper attributes."""
        super().__init__(master, fg_color="transparent", corner_radius=0)
        self._master = master
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self._id = id
        self._handler = SQLHandler()
        self._action = action
        self._entry = entry
        self.create_date_frame()
        self.create_title_frame()

    def create_date_frame(self):
        """set the proper size and location of the frame representing the date"""
        date_obj = datetime.strptime(self._entry.datenow, "%Y/%m/%d")
        date_text = date_obj.strftime("%e\n%b")
        self.date_frame = customtkinter.CTkButton(
            self, fg_color="transparent", text_color=("gray10", "gray90"), anchor="w",
            text=date_text, width=35, height=40, font=("Helvetica", 15, "bold"),
            command=self._row_pressed, corner_radius=0, hover_color=("gray70", "gray30"))
        self.date_frame.grid(row=0, column=0, rowspan=3, padx=2, pady=2, sticky='ew')

    def create_title_frame(self):
        """set the proper size and location of the frame representing the title"""
        title_text = self._wrap_title()
        self.title_frame = customtkinter.CTkButton(
            self, fg_color="transparent", text_color=("gray10", "gray90"), anchor="w",
            text=title_text, width=150, height=40, font=("Helvetica", 12), compound="right",
            command=self._row_pressed, corner_radius=0, hover_color=("gray70", "gray30"))
        self.title_frame.grid(row=0, column=1, rowspan=3, columnspan=3, padx=2, pady=2, sticky='w')

    def _wrap_title(self) -> str:
        lines = textwrap.wrap(self._entry.title, width=28)
        if len(lines) > 2:
            lines = lines[:2]
            last_line = lines[-1] + "..."
            lines = lines[:-1] + [last_line]
        return "\n".join(lines)

    def _row_pressed(self):
        self._action(self._id)
