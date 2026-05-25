# ============================================================
# Ask the user for 3 numbers.
# Print the largest number.
# ============================================================


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))



if number1 < number2:
    largest = number2
    print("The largest number is ", largest)
elif number1 < number3:
    largest = number3
    print("The largest number is ", largest)

