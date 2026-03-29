# To FEtch data from database and print them.
import sqlite3
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students LIMIT 10")
data = cursor.fetchall()

for row in data:
    print(row)
