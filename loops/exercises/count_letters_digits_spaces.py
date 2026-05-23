# count_letters_digits_spaces
# ============================================================
# Ask the user for a sentence.
#
# Count:
# - letters
# - digits
# - spaces
# ============================================================


print("# ---------- Using a for  loop ------------")

sentence = input("Enter a sentence: ")
letters = 0
digits = 0
spaces = 0
for char in sentence:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

print(f"The number of letters you entered is: {letters}")
print(f"The number of digits you entered is: {digits}")
print(f"The number of spaces you entered is: {spaces}")

print("# ---------- Using a while  loop ------------")
sentence = input("Enter a sentence: ")
letters = 0
digits = 0
spaces = 0
i = 0
while i < len(sentence):
    char = sentence[i]
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    i = i + 1

print(f"The number of letters you entered is: {letters}")
print(f"The number of digits you entered is: {digits}")
print(f"The number of spaces you entered is: {spaces}")
