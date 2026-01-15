#for counting digits of number.
num = int(input("Enter a number: "))

count = 0
temp = abs(num)   # handles negative numbers

if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10

print("Number of digits:", count)
