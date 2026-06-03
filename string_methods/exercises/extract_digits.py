# ============================================================
# File Name: extract_digits_with_check
# Description:
# Extract digits from a string and handle case where
# no digits are found.
# ============================================================

user_input = input("Enter a string: ")

digits = ""

for char in user_input:
    if char.isdigit():
        digits += char

# Check result
if digits == "":
    print("No digits found in the string.")
else:
    print(f"Extracted digits: {digits}")