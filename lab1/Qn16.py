# Factorial 

a = int(input("Enter a number for factorial:\n"))

fac = 1
for i in range(1,a+1):
    fac *= i

print("The factorial of ", a , " is ", fac)