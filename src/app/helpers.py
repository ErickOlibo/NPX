"""This module is a collection of constan and enums needed."""
from enum import Enum, auto

class View(Enum):
    """Enum listing the name of the different views in the GUI"""
    
    JOURNAL = auto()
    PLANNING = auto()
    CHALLENGES = auto()
    LOGIN = auto()
    LOGOUT = auto()