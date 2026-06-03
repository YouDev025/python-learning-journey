# ============================================================
# File Name: check_anagram
# Description:
# Check if two strings are anagrams of each other.
# An anagram means both strings contain the same letters
# with the same frequency, but in different order.
# ============================================================

# Ask the user for two words and convert to lowercase
user_input_1 = input("Enter your first word: ").lower()
user_input_2 = input("Enter your second word: ").lower()

# Compare sorted versions of both strings
if sorted(user_input_1) == sorted(user_input_2):
    print("The two strings are anagrams of each other.")
else:
    print("The two strings are not anagrams of each other.")