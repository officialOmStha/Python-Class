#put null value in db for practice.

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Set some values to NULL
cursor.execute("UPDATE students SET age = NULL WHERE id % 10 = 0")
cursor.execute("UPDATE students SET phone = NULL WHERE id % 15 = 0")

conn.commit()

