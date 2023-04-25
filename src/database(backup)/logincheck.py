import sqlite3
import hashlib

username = input('Please enter username:')
password = hashlib.sha256(input('Please enter password:').encode()).hexdigest()
conn = sqlite3.connect("../user.db")
cursor = conn.cursor()
cursor.execute("SELECT username FROM userdata "
               "WHERE username = ? AND password = ?",
               (username, password))

if not cursor.fetchone():
    print('Login failed')
else:
    print('Login successful')
