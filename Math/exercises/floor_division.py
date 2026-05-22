# Ask for two numbers and print floor division (//).

number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))

if number2 != 0:
    result = number1 // number2
    print(f"The floor division result is {result}")
else:
    print("This operation cannot be performed (division by zero)")