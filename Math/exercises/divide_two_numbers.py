# Ask for two numbers and print the division result.

number1 = float(input("first number: "))
number2 = float(input("second number: "))
if number2 !=0:
    division = number1 / number2
    print(f"division : {division:0.2f}")
else:
    print("division by zero is impossible")