# ============================================================
# Ask the user for:
# - first number
# - operator (+ - * /)
# - second number
#
# Perform the operation using if statements.
# ============================================================

while True:
    first_number = float(input("Enter a number: "))
    operator = input("Enter operator: ").split()
    second_number = float(input("Enter another number: "))

    if operator[0] == "+":
        print(f"{first_number} + {second_number} = {first_number + second_number}")
    elif operator[0] == "-":
        print(f"{first_number} - {second_number} = {first_number - second_number}")
    elif operator[0] == "*":
        print(f"{first_number} * {second_number} = {first_number * second_number}")
    elif operator[0] == "/":
        if second_number != 0:
            print(f"{first_number} / {second_number} = {first_number / second_number}")
        else :
            print("Division by zero operation impossible")
    else :
        print("Operation not supported")

    user_response = input("Do you wish to continue? (y/n): ").lower()
    if user_response in ["n" , "no" , "non"]:
        print("Exiting...")
        break

