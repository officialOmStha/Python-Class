even = False

num = int(input("Enter a number: "))

if num % 2 == 0:
    even = True

if even:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
