import random
import time
import os

os.system('color 0a')  # CMD: black background, green text

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

try:
    while True:
        line = "".join(random.choice(chars) for _ in range(80))
        print(line)
        time.sleep(0.05)
except KeyboardInterrupt:
    pass