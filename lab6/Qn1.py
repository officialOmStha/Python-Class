# to open a file and insert a line and save it.
strr = "Hello World."


with open("Example.txt", "w") as fi:
    fi.write(strr)
print("file written")

# to apend
with open("Example.txt", "a") as fi:
    fi.write("\nThis is a new line.")

# to read the content of a file.
file = open("Example.txt", "r")
content = file.read()
print(content)
file.close()




