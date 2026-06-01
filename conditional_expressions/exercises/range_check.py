# Name: range_check
# Description:
# Ask the user for a number.
# Use a ternary operator to determine whether the number
# is between 1 and 100 inclusive.
# Display:
# "In Range" or "Out of Range".
# ============================================================


number = float(input("Please enter a number: "))
range_check = "In Range" if 1 <= number <= 100 else "Out of Range"

print(f"Your {number} is {range_check} [1 -100]")
