# Qn 2 with os module.
import os
# File path
file_path = "Example.txt"

# Check if file exists
if os.path.exists(file_path):
    print("Filename:", os.path.basename(file_path))
    print("Absolute Path:", os.path.abspath(file_path))
    print("Size (bytes):", os.path.getsize(file_path))
    print("Is File?", os.path.isfile(file_path))
    print("Is Directory?", os.path.isdir(file_path))
else:
    print(f"The file '{file_path}' does not exist.")