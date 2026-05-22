# Ask for two numbers and print the remainder (%).

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if number2 != 0:
    remainder = number1 % number2
    print(f"The remainder is {remainder}")
else:
    print("This operation cannot be performed because division by zero is not allowed.")
    