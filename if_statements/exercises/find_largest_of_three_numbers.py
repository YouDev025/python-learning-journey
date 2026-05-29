# ============================================================
# Ask the user for 3 numbers.
# Print the largest number.
# ============================================================


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))



if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3


print("The largest number is", largest)