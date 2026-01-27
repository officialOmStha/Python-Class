num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

def check(x,y):
    if x == y:
        return True
    else:
        return False 
    
print(check(num1,num2))