# ============================================================
# 1. WHAT IS A CONDITIONAL EXPRESSION?
# ============================================================
# A conditional expression (ternary operator) is a one-line
# shortcut for an if-else statement.
#
# Syntax:
#
# value_if_true if condition else value_if_false
#
# Python evaluates the condition:
# - If True  -> returns value_if_true
# - If False -> returns value_if_false
# ============================================================


# ============================================================
# 2. BASIC EXAMPLE
# ============================================================

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)

# Output:
# Adult


# ============================================================
# 3. EQUIVALENT IF-ELSE
# ============================================================

age = 20

if age >= 18:
    result = "Adult"
else:
    result = "Minor"

print(result)

# Output:
# Adult


# ============================================================
# 4. EVEN OR ODD
# ============================================================

num = 6

result = "Even" if num % 2 == 0 else "Odd"

print(result)

# Output:
# Even


# ============================================================
# 5. POSITIVE OR NEGATIVE
# ============================================================

num = -10

result = "Positive" if num > 0 else "Negative"

print(result)

# Output:
# Negative


# ============================================================
# 6. PASS OR FAIL
# ============================================================

score = 70

result = "Pass" if score >= 50 else "Fail"

print(result)

# Output:
# Pass


# ============================================================
# 7. ACCESS CONTROL
# ============================================================

is_logged_in = True

result = "Access Granted" if is_logged_in else "Access Denied"

print(result)

# Output:
# Access Granted


# ============================================================
# 8. COMPARISON OPERATORS USED IN CONDITIONS
# ============================================================
#
# ==   Equal
# !=   Not Equal
# >    Greater Than
# <    Less Than
# >=   Greater Than or Equal
# <=   Less Than or Equal
#
# These operators return True or False.
# ============================================================

num = 10

print(num == 10)
print(num != 10)
print(num > 5)
print(num < 5)

# Output:
# True
# False
# True
# False


# ============================================================
# 9. USING LOGICAL OPERATORS
# ============================================================
#
# and
# or
# not
#
# ============================================================

age = 25
has_id = True

result = (
    "Access Granted"
    if age >= 18 and has_id
    else "Access Denied"
)

print(result)

# Output:
# Access Granted


# ============================================================
# 10. USING OR
# ============================================================

username = "admin"

result = (
    "Authorized"
    if username == "admin" or username == "root"
    else "Unauthorized"
)

print(result)

# Output:
# Authorized


# ============================================================
# 11. USING NOT
# ============================================================

is_banned = False

result = (
    "Welcome"
    if not is_banned
    else "Blocked"
)

print(result)

# Output:
# Welcome


# ============================================================
# 12. STRING COMPARISON
# ============================================================

password = "python123"

result = (
    "Correct Password"
    if password == "python123"
    else "Wrong Password"
)

print(result)

# Output:
# Correct Password


# ============================================================
# 13. MEMBERSHIP TEST
# ============================================================
#
# in
# not in
#
# ============================================================

username = "admin"

result = (
    "Admin Access"
    if username in ["admin", "root", "manager"]
    else "Standard User"
)

print(result)

# Output:
# Admin Access


# ============================================================
# 14. RANGE CHECK
# ============================================================

number = 50

result = (
    "In Range"
    if 1 <= number <= 100
    else "Out of Range"
)

print(result)

# Output:
# In Range


# ============================================================
# 15. FIND LARGER NUMBER
# ============================================================

a = 10
b = 20

largest = a if a > b else b

print(largest)

# Output:
# 20


# ============================================================
# 16. FIND SMALLER NUMBER
# ============================================================

a = 10
b = 20

smallest = a if a < b else b

print(smallest)

# Output:
# 10


# ============================================================
# 17. NESTED TERNARY OPERATOR
# ============================================================
#
# Used for multiple conditions.
#
# Syntax:
#
# value1 if condition1
# else value2 if condition2
# else value3
#
# ============================================================

num = 0

result = (
    "Positive"
    if num > 0
    else "Negative"
    if num < 0
    else "Zero"
)

print(result)

# Output:
# Zero


# ============================================================
# 18. GRADE SYSTEM WITH NESTED TERNARY
# ============================================================

score = 85

grade = (
    "A"
    if score >= 90
    else "B"
    if score >= 80
    else "C"
    if score >= 70
    else "F"
)

print(grade)

# Output:
# B


# ============================================================
# 19. USER INPUT EXAMPLE
# ============================================================

age = int(input("Enter your age: "))

result = "Adult" if age >= 18 else "Minor"

print(result)


# ============================================================
# 20. MOST COMMON INTERVIEW QUESTIONS
# ============================================================

# Even or Odd

num = 7

result = "Even" if num % 2 == 0 else "Odd"

print(result)


# Positive or Negative

num = -5

result = "Positive" if num > 0 else "Negative"

print(result)


# Pass or Fail

score = 45

result = "Pass" if score >= 50 else "Fail"

print(result)


# Adult or Minor

age = 17

result = "Adult" if age >= 18 else "Minor"

print(result)


# ============================================================
# 21. BEST PRACTICES
# ============================================================
#
# ✓ Use ternary operators for simple decisions.
#
# ✓ Use normal if-else blocks for complex logic.
#
# ✓ Keep ternary expressions short and readable.
#
# ✓ Avoid deeply nested ternary expressions.
#
# ✗ Bad:
#
# result = "A" if x > 90 else "B" if x > 80 else \
#          "C" if x > 70 else "D" if x > 60 else "F"
#
# ✓ Better:
#
# Use if-elif-else.
#
# ============================================================


# ============================================================
# SUMMARY
# ============================================================
#
# Syntax:
#
# value_if_true if condition else value_if_false
#
# Examples:
#
# "Even" if num % 2 == 0 else "Odd"
#
# "Adult" if age >= 18 else "Minor"
#
# "Pass" if score >= 50 else "Fail"
#
# a if a > b else b
#
# ============================================================
# END OF FILE
# ============================================================