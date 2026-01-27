#count no of vowels

# count number of vowels

string = input("Enter a sentence or a word:\n")

vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vow_no = 0

for ch in string:
    if ch in vowel:
        vow_no += 1

print(f"The number of vowel letters are: {vow_no}")
