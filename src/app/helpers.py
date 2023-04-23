"""This module is a collection of constan and enums needed."""
from enum import Enum, auto

class View(Enum):
    """Enum listing the name of the different views in the GUI"""
    
    JOURNAL = auto()
    PLANNING = auto()
    CHALLENGES = auto()
    LOGIN = auto()
    LOGOUT = auto()


SAMPLE_ENTRIES = {
    0: ["Sat 8 April", "A Sunny Day", ("Stress", "Anger"),
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..."],
    1: ["Wed 5 April", "Waiting for the Results", ("Anxiety", "Panic", "Not eating"),
        "Ut etiam sit amet nisl purus in mollis. Donec massa sapien faucibus et molestie ac feugiat..."],
    2: ["Mon 27 March", "Not Sure How I Feel", (),
        "Sed augue lacus viverra vitae congue eu consequat. Lacinia quis vel eros donec ac. At quis risus sed vulputate odio ut enim...."],
}