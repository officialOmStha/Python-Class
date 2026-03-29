# To Create Table in database withpython. 
import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    age INTEGER,
    phone TEXT
)
""")

print("Table created successfully")