# Name: even_or_odd
# Description:
# Ask the user for a number.
# Use a ternary operator to determine whether the number
# is Even or Odd.
# ============================================================


number = int(input("Enter a number: "))
parity = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {parity}")