s = {1, 2, 3, 4, 5}
fs = {3,4,5,6,7,8}

s.add(6)
s.update({7,8,9})

for val in s:
    print(val)


print(s | fs)
print(s & fs)
print(s - fs)
print(s ^ fs)
