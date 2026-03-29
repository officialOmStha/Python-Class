import sqlite3
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

name = input("enter name to search: ")

cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
print(cursor.fetchall())