# Name: larger_number
# Description:
# Ask the user for two numbers.
# Use a ternary operator to find and display
# the larger number.
# ============================================================

number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))

larger_number = number1 if number1 > number2 else number2

print(f"Your largest number is: {larger_number}")