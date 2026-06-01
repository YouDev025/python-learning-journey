# Name: smaller_number
# Description:
# Ask the user for two numbers.
# Use a ternary operator to find and display
# the smaller number.
# ============================================================



number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))


smaller_number = number1 if number1 < number2 else number2

print(f"Your smaller number is {smaller_number}")