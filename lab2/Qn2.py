def check(x):
    print("Function/Method called for value: ", x)
    return True if x > 0 else False

a= check
b = check 
c = check


if a(-10) or b(20) or c(2):
    print("Atleast one True")
else:
    print("None correct.")