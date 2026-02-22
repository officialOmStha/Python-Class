# filehandling with exception handling
import os


file_path = "Example.txt"
try:
    # 1️⃣ Check if file exists
    if not os.path.exists(file_path):
        print("File does not exist. Creating file...")
        with open(file_path, "w") as f:
            f.write("Hello World\n")
    else:
        print("File already exists.")

    # 2️⃣ Append data
    with open(file_path, "a") as f:
        f.write("This is appended line.\n")

    # 3️⃣ Read file
    with open(file_path, "r") as f:
        print("\nFile Content:")
        print(f.read())

    # 4️⃣ File properties using os
    print("\nFile Properties:")
    print("File Name:", os.path.basename(file_path))
    print("Absolute Path:", os.path.abspath(file_path))
    print("File Size:", os.path.getsize(file_path), "bytes")

    # 5️⃣ Delete file
    os.remove(file_path)
    print("\nFile deleted successfully.")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("\nProgram execution completed.")