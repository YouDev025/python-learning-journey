# ============================================================
# File Name: count_vowels
# Description:
# Ask the user for a string and count how many vowels
# (a, e, i, o, u) it contains.
# ============================================================

# Ask the user to enter a string
user_string = input("Enter a string: ")

# Define the vowels
vowels = "aeiouAEIOU"

# Initialize the vowel counter
vowel_count = 0

# Check each character in the string
for char in user_string:
    if char in vowels:
        print(f"{char} is a vowel")
        vowel_count += 1

# Display the total number of vowels
print(f"\n'{user_string}' has {vowel_count} vowels.")