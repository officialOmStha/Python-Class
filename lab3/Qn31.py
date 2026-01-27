my_list = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates by converting to a set
my_set = set(my_list)
print("As set (duplicates removed):", my_set)

# Convert back to list if needed
unique_list = list(my_set)
print("As list:", unique_list)
