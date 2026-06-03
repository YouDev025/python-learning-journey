# ============================================================
# Ask the user for a string and reverse it using:
# 1. Python slicing
# 2. A loop
# Then display the results of both methods.
# ============================================================

# Ask the user to enter a string
user_string = input("Enter a string: ")

# ============================================================
# Method 1: Reverse the string using slicing
# Syntax: string[start:stop:step]
# A step of -1 means move backward through the string.
# ============================================================
reversed_string_slice = user_string[::-1]

# ============================================================
# Method 2: Reverse the string using a loop
# Create an empty string and build the reversed version
# by adding each character to the beginning.
# ============================================================
reversed_string_loop = ""

for char in user_string:
    reversed_string_loop = char + reversed_string_loop

# ============================================================
# Display the results
# ============================================================
print("\nOriginal String:", user_string)
print("Reversed (Slicing):", reversed_string_slice)
print("Reversed (Loop):", reversed_string_loop)