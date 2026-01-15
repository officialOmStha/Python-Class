#sum of natural numbers up to n 

n = int(input("Enter a number upto which you want sum of natural number: \n"))

sum = 0
for i in range(1,n+1):
    sum += i

print("The sum of naturan number is: ", sum)