# ============================================
# Exercise 17: simple_calculator
# ============================================

# Ask the user for:
# first number
# second number
#
# Print:
# addition
# subtraction
# multiplication
# division

first_number , second_number = map(float , input("Entrer 2 numbers separated with space :  ").split())

addition = first_number + second_number
print(f"The addition of {first_number} and {second_number} is {addition}")

subtraction = first_number - second_number
print(f"The substraction of {first_number} and {second_number} is {subtraction}")

multiplication =first_number * second_number
print(f"The multiplication of {first_number} and {second_number} is {multiplication}")

if second_number != 0:
    division = first_number / second_number
    print(f"The division of {first_number} by {second_number} is {division}")
else:
    print("The division by ZERO is impossible")

