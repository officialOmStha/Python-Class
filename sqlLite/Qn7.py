# Fill Missing Values
import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT AVG(age) FROM students")
avg_age = cursor.fetchone()[0]

cursor.execute("UPDATE students SET age = ? WHERE age IS NULL", (avg_age,))
cursor.execute("UPDATE students SET phone = '9800000000' WHERE phone IS NULL")

conn.commit()