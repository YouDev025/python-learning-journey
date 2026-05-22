# Ask for two numbers and swap them.

number1 =float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
print(f"The number before swap them are {number1:0.2f} and {number2:0.2f}")

number1 , number2 = number2 , number1
print(f"The number after swap them are {number1:0.2f} and {number2:0.2f}")