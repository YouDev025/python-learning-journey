# Ask for a number and print its cube (n * n * n).

number = float(input("Enter a number: "))
cube = number ** 3 # or use cube = number * number * number
print(f"The cube of {number} is {cube:0.2f}")