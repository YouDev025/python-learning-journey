# ============================================
# USER INPUT IN PYTHON
# ============================================
# This file contains everything you need to know
# about user input in Python.
#
# All explanations are written as comments
# so you can use this file as documentation
# while learning.
# ============================================


# ============================================
# 1. WHAT IS USER INPUT?
# ============================================
# User input allows a program to receive data
# from the keyboard while the program is running.
#
# Python uses the input() function to get input.
#
# Syntax:
# variable = input("Message")
#
# Example:
# name = input("Enter your name: ")
#
# The text inside input() is called a prompt.
# It tells the user what to enter.


# ============================================
# 2. SIMPLE INPUT EXAMPLE
# ============================================

name = input("Enter your name: ")

print("Hello", name)


# ============================================
# 3. IMPORTANT NOTE:
# input() ALWAYS RETURNS A STRING
# ============================================
# Even if the user types a number,
# Python stores it as text (string).
#
# Example:
# age = input("Enter age: ")
#
# If user enters: 20
#
# age becomes:
# "20"  -> string, NOT integer


# ============================================
# 4. CHECKING THE TYPE OF INPUT
# ============================================

age = input("Enter your age: ")

print(type(age))


# ============================================
# 5. CONVERTING INPUT TO INTEGER
# ============================================
# To use numbers in calculations,
# convert the input using int().
#
# Syntax:
# int(variable)

age = int(input("Enter your age: "))

print(age)
print(type(age))


# ============================================
# 6. CONVERTING INPUT TO FLOAT
# ============================================
# float() converts input into decimal numbers.

price = float(input("Enter product price: "))

print(price)
print(type(price))


# ============================================
# 7. MULTIPLE INPUTS
# ============================================

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print("Full name:", first_name, last_name)


# ============================================
# 8. INPUT + MATHEMATICAL OPERATIONS
# ============================================

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2

print("Sum =", sum_result)


# ============================================
# 9. INPUT + SUBTRACTION
# ============================================

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

result = a - b

print("Result =", result)


# ============================================
# 10. INPUT + MULTIPLICATION
# ============================================

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

multiplication = x * y

print("Multiplication =", multiplication)


# ============================================
# 11. INPUT + DIVISION
# ============================================

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

division = number1 / number2

print("Division =", division)


# ============================================
# 12. STRING CONCATENATION WITH INPUT
# ============================================

city = input("Enter your city: ")

message = "You live in " + city

print(message)


# ============================================
# 13. USING F-STRINGS WITH INPUT
# ============================================
# f-strings are cleaner and easier to read.

language = input("Enter favorite language: ")

print(f"Your favorite language is {language}")


# ============================================
# 14. BOOLEAN INPUT
# ============================================
# input() does NOT directly return True or False.
#
# Example:
# is_student = input("Are you a student? ")
#
# If user enters:
# yes
#
# The result is:
# "yes" -> string

answer = input("Are you a student? ")

print(answer)
print(type(answer))


# ============================================
# 15. COMPARING INPUT VALUES
# ============================================

password = input("Enter password: ")

if password == "python123":
    print("Access granted")
else:
    print("Wrong password")


# ============================================
# 16. USING LOWER() WITH INPUT
# ============================================
# lower() converts text to lowercase.
#
# Useful for avoiding problems with uppercase/lowercase.

color = input("Enter your favorite color: ").lower()

if color == "blue":
    print("Nice color!")
else:
    print("Different color")


# ============================================
# 17. USING STRIP() WITH INPUT
# ============================================
# strip() removes spaces before and after text.

username = input("Enter username: ").strip()

print(username)


# ============================================
# 18. MULTIPLE VALUES IN ONE INPUT
# ============================================
# split() separates values using spaces.

first, second = input("Enter two numbers: ").split()

print(first)
print(second)


# ============================================
# 19. MULTIPLE NUMBERS WITH MAP()
# ============================================
# map() applies a function to multiple values.
#
# Very common in Python.

num1, num2 = map(int, input("Enter two numbers: ").split())

print(num1 + num2)


# ============================================
# 20. INPUT VALIDATION
# ============================================
# Validation checks if input is correct.

age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# ============================================
# 21. COMMON ERROR:
# VALUEERROR
# ============================================
# Happens when conversion fails.
#
# Example:
# int("hello")
#
# ERROR:
# ValueError


# ============================================
# 22. HANDLING ERRORS WITH TRY/EXCEPT
# ============================================

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input")


# ============================================
# 23. INPUT INSIDE LOOPS
# ============================================

while True:
    number = input("Type 'exit' to stop: ")

    if number == "exit":
        break

    print("You typed:", number)


# ============================================
# 24. SECRET PASSWORD LOOP
# ============================================

while True:
    password = input("Enter password: ")

    if password == "admin":
        print("Correct password")
        break
    else:
        print("Try again")


# ============================================
# 25. USER INPUT + LIST
# ============================================

items = input("Enter shopping items separated by commas: ")

shopping_list = items.split(",")

print(shopping_list)


# ============================================
# 26. USER INPUT + TYPE CASTING SUMMARY
# ============================================
#
# str()   -> convert to string
# int()   -> convert to integer
# float() -> convert to decimal number
# bool()  -> convert to boolean
#
# Examples:
#
# str(100)
# int("50")
# float("5.5")
# bool(1)


# ============================================
# 27. IMPORTANT NOTES
# ============================================
#
# input() always returns STRING data.
#
# Use int() for whole numbers.
#
# Use float() for decimal numbers.
#
# Use split() for multiple values.
#
# Use lower() to ignore uppercase/lowercase.
#
# Use strip() to remove spaces.
#
# Use try/except to avoid program crashes.
#
# Always validate user input when possible.





# ============================================
# END OF USER INPUT NOTES
# ============================================