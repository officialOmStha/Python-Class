set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


# Using union() method
union_set = set1.union(set2)

# Or using | operator
union_set2 = set1 | set2

print("Union:", union_set)
print("Union using | :", union_set2)


# Using intersection() method
intersection_set = set1.intersection(set2)

# Or using & operator
intersection_set2 = set1 & set2

print("Intersection:", intersection_set)
print("Intersection using & :", intersection_set2)


# Using difference() method
diff_set = set1.difference(set2)

# Or using - operator
diff_set2 = set1 - set2

print("Difference (set1 - set2):", diff_set)



# Using symmetric_difference() method
sym_diff = set1.symmetric_difference(set2)

# Or using ^ operator
sym_diff2 = set1 ^ set2

print("Symmetric Difference:", sym_diff)
print("Symmetric Difference using ^ :", sym_diff2)
