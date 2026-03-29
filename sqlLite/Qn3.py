# Insert 100+ records in the table with python.

import random
import string
import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

def random_name():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

def random_address():
    return "Street-" + str(random.randint(1, 50))

def random_phone():
    prefixes = ["98", "97", "95", "96", "94"]
    return random.choice(prefixes) + ''.join(random.choices(string.digits, k=8))

# Insert 120 records
for _ in range(120):
    cursor.execute("""
    INSERT INTO students (name, address, age, phone)
    VALUES (?, ?, ?, ?)
    """, (
        random_name(),
        random_address(),
        random.randint(18, 60),
        random_phone()
    ))

conn.commit()
print("Data inserted successfully")