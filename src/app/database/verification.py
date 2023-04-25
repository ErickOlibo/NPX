import hashlib
import sqlite3
from tkinter import messagebox


class Verification:
    def __init__(self):
        self.conn = sqlite3.connect("user.db")
        self.cursor = self.conn.cursor()

    def verify_user(self, user, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute("SELECT username FROM userdata "
                            "WHERE username = ? AND password = ?",
                            (user, hashed_password))
        if not self.cursor.fetchone():
            messagebox.showerror("Error", "Invalid username or password.")
        else:
            return True
