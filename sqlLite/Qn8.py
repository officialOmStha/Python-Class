# Fill Missing Values
import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM students
WHERE phone NOT LIKE '98%' 
AND phone NOT LIKE '97%' 
AND phone NOT LIKE '95%'
""")

filtered = cursor.fetchall()
print("Filtered rows:", len(filtered))