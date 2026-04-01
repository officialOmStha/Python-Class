# Function to get prime number up to user input.

num = int(input("Enter number up to which you need prome number: "))
prime_list = ""

for i in range(1,num +1):
    prime = True
    for j in range(2,i):
        if i <= 2:
            prime = True
        elif i % j == 0:
            prime = False
    if prime:
        prime_list += str(i) + ","

print(prime_list)