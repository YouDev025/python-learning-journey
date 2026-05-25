# Ask the user for two numbers.
# Print which one is greater.
# If equal, print "Both are equal".
# ============================================================

number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))

if number1 > number2:
    print(f"{number1} > {number2}")
elif number1 < number2:
    print(f"{number1} < {number2}")
else:
    print(f"{number1} =  {number2}")