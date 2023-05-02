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
        text VARCHAR(1000),
        date DATE,
        time TIME,
        tags VARCHAR(255)
        )
    """


class IssueMessage(Enum):
    """Enum listing the different issues that can occur during startup"""
    USERNAME_TAKEN = "Username Already Taken!"
    WRONG_USERNAME = "Wrong Username!"
    WRONG_PASSWORD = "Wrong Password!"
    EMPTY_USERNAME = "Username Field is Empty!"
    EMPTY_PASSWORD = "Password Field is Empty!"
    WEAK_PASSWORD = "The Password is too Short\n16 charaters minimum!"
    MISSING_SPECIAL = "Password needs one special\ncharacter:'!@#$%^&?*'!"
    UNKNOWN = "Unknown Issue!"
    NONE = "None"


    @property
    def type(self) -> StartUp:
        """
        Return the Startup type (Login or Sign in) of the current session.

        Returns:
        - StartUp: the type choosen.
        """
        return self._type

