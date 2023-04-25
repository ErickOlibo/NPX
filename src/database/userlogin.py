import sqlite3
import hashlib

conn = sqlite3.connect("user.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS userdata(
    id INTEGER PRIMARY KEY,
    username VARCHARD(255) NOT NULL,
    password VARCHARD(255) NOT NULL,
    UNIQUE(username)
)
""")

user1 = 'michaeliay'
password1 = hashlib.sha256('michaelia123'.encode()).hexdigest()
user2 = 'miki233'
password2 = hashlib.sha256('michaelia456'.encode()).hexdigest()

cursor.execute("INSERT OR IGNORE INTO userdata (username, password) "
               "VALUES (?, ?)",
               (user1, password1))

cursor.execute("INSERT OR IGNORE INTO userdata (username, password) "
               "VALUES (?, ?)",
               (user2, password2))

conn.commit()
