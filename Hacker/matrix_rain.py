import random
import os
import time
import shutil

# Set CMD colors: black background, green text
os.system('color 0a')

# Get terminal size
columns, rows = shutil.get_terminal_size()

# Characters to display
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

# Initialize drops for each column
drops = [0 for _ in range(columns)]

try:
    while True:
        line = ""
        for i in range(columns):
            if drops[i] == 0:
                line += " "
            else:
                line += random.choice(chars)
            
            # Randomly reset drop
            if drops[i] > random.randint(rows//2, rows):
                drops[i] = 0
            else:
                drops[i] += 1

        print(line)
        time.sleep(0.05)
except KeyboardInterrupt:
    os.system('cls')
    print("Matrix effect stopped.")