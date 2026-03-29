# To FEtch data from database and print them.
import sqlite3
name = input("enter name to search: ")
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students LIMIT 10")
data = cursor.fetchall()

cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
data = cursor.fetchall()

for row in data:
    print(row)
