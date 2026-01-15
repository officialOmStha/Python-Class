#reverse the number

num = int(input("Enter a number: "))

rev = 0
temp = abs(num)   # handle negative numbers

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

# restore sign if number was negative
rev = -rev if num < 0 else rev

print("Reversed number:", rev)
