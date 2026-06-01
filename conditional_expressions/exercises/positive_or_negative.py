# Name: positive_or_negative
# Description:
# Ask the user for a number.
# Use a ternary operator to determine whether the number
# is Positive or Negative.
# ============================================================



number = float(input("Please enter a number: "))

is_positive = "Positive" if number > 0 else  "Negative" if number < 0 else "Null"


print(f"{number} is {is_positive}")