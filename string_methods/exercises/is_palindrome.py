# ============================================================
# File Name: palindrome_checker
# Description:
# Ask the user for a string and check whether it is
# a palindrome (reads the same forward and backward).
# ============================================================

# Ask the user to enter a string
user_input = input("Enter a string: ")

# Reverse the string using slicing
reversed_string = user_input[::-1]

# Compare the original string with the reversed string
if user_input == reversed_string:
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")