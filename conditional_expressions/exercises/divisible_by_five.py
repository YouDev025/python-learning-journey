# Name: divisible_by_five
# Description:
# Ask the user for a number.
# Use a ternary operator to determine whether the number
# is divisible by 5.
# ============================================================



number = float(input("Enter a number: "))

divisible_by_five = "Divisible by 5" if number % 5 == 0 else "not Divisible by 5"

print(f"Your {number} is {divisible_by_five}")