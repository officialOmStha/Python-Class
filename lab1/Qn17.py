a = [1,2,3,4,5]

b = int(input("Enter a number to find in a list"))

for i in a:
    if (a[i] == b):
        print(b, " is at index ", i, ".")
        break
    else:
        print(b," not found")