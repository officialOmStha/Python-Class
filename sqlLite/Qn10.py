# To update

import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute("UPDATE students SET age = 25 Where id = 1")
conn.commit()

cursor.execute("SELECT * FROM students WHERE id = 1")
data = cursor.fetchall()
print(data)