# ============================================================
# if_statements_complete_guide 
# ============================================================
# EVERYTHING YOU NEED TO KNOW ABOUT:
# if, elif, else in Python
#
# This file contains:
# 1. Basic if statements
# 2. if-else
# 3. if-elif-else
# 4. Comparison operators
# 5. Logical operators
# 6. Nested if statements
# 7. Short-hand if
# 8. Ternary operator
# 9. Common mistakes
# 10. Real examples
#
# NOTE:
# Python uses INDENTATION instead of {} braces.
# Indentation is VERY IMPORTANT.
# ============================================================


# ============================================================
# 1. BASIC IF STATEMENT
# ============================================================

# The "if" statement checks if a condition is True.
# If True -> the code inside runs.
# If False -> the code is skipped.

age = 20

if age >= 18:
    print("You are an adult")

# Output:
# You are an adult


print("\n")


# ============================================================
# 2. IF-ELSE STATEMENT
# ============================================================

# "else" runs when the condition is False.

temperature = 15

if temperature > 25:
    print("It is hot")
else:
    print("It is cold")

# Output:
# It is cold


print("\n")


# ============================================================
# 3. IF-ELIF-ELSE STATEMENT
# ============================================================

# "elif" means:
# "else if"

# It allows checking multiple conditions.

score = 75

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Failed")

# Output:
# Grade C


print("\n")


# ============================================================
# 4. COMPARISON OPERATORS
# ============================================================

# Comparison operators compare values.

# ==   Equal to
# !=   Not equal to
# >    Greater than
# <    Less than
# >=   Greater than or equal to
# <=   Less than or equal to

a = 10
b = 5

if a > b:
    print("a is greater than b")

if a != b:
    print("a and b are different")

if b < a:
    print("b is smaller than a")


print("\n")


# ============================================================
# 5. LOGICAL OPERATORS
# ============================================================

# Logical operators combine conditions.

# and  -> BOTH conditions must be True
# or   -> AT LEAST ONE condition must be True
# not  -> reverses the result

age = 25
has_ticket = True

# ---------- AND ----------
if age >= 18 and has_ticket:
    print("You can enter")

# ---------- OR ----------
is_weekend = False

if age < 18 or is_weekend:
    print("Special rule activated")
else:
    print("Normal rule")

# ---------- NOT ----------
is_raining = False

if not is_raining:
    print("Go outside")


print("\n")


# ============================================================
# 6. NESTED IF STATEMENTS
# ============================================================

# Nested means:
# an if statement INSIDE another if statement.

username = "admin"
password = "1234"

if username == "admin":

    # This if runs only if the first condition is True
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")

else:
    print("Wrong username")


print("\n")


# ============================================================
# 7. SHORT-HAND IF
# ============================================================

# You can write simple if statements in one line.

number = 10

if number > 0: print("Positive number")


print("\n")


# ============================================================
# 8. SHORT-HAND IF-ELSE (TERNARY OPERATOR)
# ============================================================

# Syntax:
# value_if_true if condition else value_if_false

age = 16

message = "Adult" if age >= 18 else "Minor"

print(message)

# Output:
# Minor


print("\n")


# ============================================================
# 9. USING INPUT WITH IF STATEMENTS
# ============================================================

# input() always returns TEXT (string).
# Use int() if you need numbers.

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")


print("\n")


# ============================================================
# 10. CHECKING EVEN OR ODD
# ============================================================

# % is the modulo operator.
# It gives the remainder.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


print("\n")


# ============================================================
# 11. MULTIPLE CONDITIONS
# ============================================================

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Access granted")
else:
    print("Access denied")


print("\n")


# ============================================================
# 12. MEMBERSHIP OPERATORS
# ============================================================

# "in" checks if something exists inside another thing.

letter = "a"

if letter in "apple":
    print("Letter found")

# "not in" checks if something does NOT exist.

if "z" not in "apple":
    print("z does not exist")


print("\n")


# ============================================================
# 13. BOOLEAN VALUES
# ============================================================

# Boolean values are:
# True
# False

is_logged_in = True

if is_logged_in:
    print("Welcome back")

# Same as:
# if is_logged_in == True:

# But shorter and cleaner.


print("\n")


# ============================================================
# 14. CHAINED COMPARISONS
# ============================================================

# Python allows multiple comparisons together.

age = 25

if 18 <= age <= 30:
    print("Young adult")


print("\n")


# ============================================================
# 15. COMMON MISTAKES
# ============================================================

# ---------- MISTAKE 1 ----------
# Using = instead of ==

# WRONG:
# if age = 18:

# CORRECT:
# if age == 18:


# ---------- MISTAKE 2 ----------
# Forgetting indentation

# WRONG:
#
# if age > 18:
# print("Adult")

# CORRECT:
#
# if age > 18:
#     print("Adult")


# ---------- MISTAKE 3 ----------
# Comparing input() directly with numbers

# WRONG:
#
# age = input("Age: ")
# if age > 18:

# CORRECT:
#
# age = int(input("Age: "))
# if age > 18:


print("Common mistakes section completed")


print("\n")


# ============================================================
# 16. REAL EXAMPLE — SIMPLE ATM
# ============================================================

balance = 1000
withdraw = int(input("Enter amount to withdraw: "))

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")


print("\n")


# ============================================================
# 17. REAL EXAMPLE — LOGIN SYSTEM
# ============================================================

saved_username = "admin"
saved_password = "1234"

entered_username = input("Username: ")
entered_password = input("Password: ")

if entered_username == saved_username:

    if entered_password == saved_password:
        print("Login successful")
    else:
        print("Incorrect password")

else:
    print("Username not found")


print("\n")


# ============================================================
# 18. REAL EXAMPLE — GRADE CALCULATOR
# ============================================================

grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Excellent")
elif grade >= 75:
    print("Good")
elif grade >= 50:
    print("Pass")
else:
    print("Fail")


print("\n")


# ============================================================
# 19. TRUTHY AND FALSY VALUES
# ============================================================

# Some values are automatically considered False:
#
# False
# 0
# ""
# []
# None

# Everything else is usually True.

name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")


print("\n")


# ============================================================
# 20. FINAL SUMMARY
# ============================================================

# if    -> checks a condition
# elif  -> checks another condition
# else  -> runs if all conditions are False
#
# IMPORTANT OPERATORS:
#
# ==  equal
# !=  not equal
# >   greater than
# <   less than
# >=  greater or equal
# <=  less or equal
#
# LOGICAL OPERATORS:
#
# and
# or
# not
#
# REMEMBER:
#
# - Python uses indentation
# - Conditions return True or False
# - input() returns strings
# - Use int() for numbers
#
# Practice a lot to master if statements.
# ============================================================

print("End of tutorial")