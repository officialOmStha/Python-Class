# Find missing values indatabase.
import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students WHERE age IS NULL OR phone IS NULL")
missing = cursor.fetchall()

print("Missing rows:", len(missing))