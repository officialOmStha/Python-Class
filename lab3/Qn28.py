my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)


my_set.add(6)
print("After adding 6:", my_set)

my_set.update([7, 8, 9])
print("After adding [7, 8, 9]:", my_set)

my_set.remove(3)
print("After removing 3:", my_set)


my_set.discard(10)  # 10 not in set, but no error
print("After discarding 10:", my_set)



