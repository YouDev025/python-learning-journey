# ============================================
# Exercise 6: two_number_division
# ============================================

# Ask the user for two float numbers
# Print the division result


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
if number2 != 0:
    division = number1 / number2
    print(f"The division of {number1} and {number2} is {division:0.2f}")
else:
    print("The division by 0 is not possible")