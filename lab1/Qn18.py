# Number is prime or not.
a = int(input("Enter a number:\n"))

i = 2
prime = True

for i in range(2,a):
    if(a % i == 0):
        prime = False

if(prime):
    print(a, " is a prime number")
else:
    print(a, " is not a prime number")
