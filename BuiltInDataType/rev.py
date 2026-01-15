#we get a number.
#we divide num by 10 and store remainder in rev and store flore in temp.

def rev(x):
    temp = 0
    revv = 0
    

    while x != 0:
        temp = x % 10
        revv = revv * 10 + temp
        x = x // 10
    
    return revv


print(rev(123))