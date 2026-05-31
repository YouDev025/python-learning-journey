# ============================================================
# LOGICAL OPERATORS IN PYTHON
# ============================================================
# Logical operators are used to combine conditional statements.
#
# Python has 3 logical operators:
# 1. and
# 2. or
# 3. not
#
# They return either True or False.
# ============================================================


# ============================================================
# 1. THE "and" OPERATOR
# ============================================================
# Returns True only if BOTH conditions are True.
#
# Truth Table:
#
# Condition A | Condition B | A and B
# -----------------------------------
#    True     |    True     |  True
#    True     |    False    |  False
#    False    |    True     |  False
#    False    |    False    |  False
# ============================================================

age = 20
has_id = True

print(age >= 18 and has_id)
# True because BOTH conditions are True

print(age >= 18 and False)
# False because one condition is False


# Example: Login System
username = "admin"
password = "1234"

print(username == "admin" and password == "1234")
# True


# ============================================================
# 2. THE "or" OPERATOR
# ============================================================
# Returns True if AT LEAST ONE condition is True.
#
# Truth Table:
#
# Condition A | Condition B | A or B
# ----------------------------------
#    True     |    True     |  True
#    True     |    False    |  True
#    False    |    True     |  True
#    False    |    False    |  False
# ============================================================

is_weekend = False
is_holiday = True

print(is_weekend or is_holiday)
# True because one condition is True

print(False or False)
# False because both are False


# Example: User Access
role = "admin"

print(role == "admin" or role == "manager")
# True


# ============================================================
# 3. THE "not" OPERATOR
# ============================================================
# Reverses (negates) a Boolean value.
#
# Truth Table:
#
# Original Value | not Value
# --------------------------
#      True      |   False
#      False     |   True
# ============================================================

logged_in = True

print(not logged_in)
# False

print(not False)
# True


# Example
is_banned = False

print(not is_banned)
# True
# User is NOT banned


# ============================================================
# COMBINING LOGICAL OPERATORS
# ============================================================
# You can combine multiple logical operators together.
# ============================================================

age = 25
has_ticket = True
is_vip = False

print(age >= 18 and (has_ticket or is_vip))
# True

# Step 1:
# (has_ticket or is_vip)
# True or False
# -> True
#
# Step 2:
# age >= 18 and True
# True and True
# -> True


# ============================================================
# OPERATOR PRECEDENCE
# ============================================================
# Python evaluates logical operators in this order:
#
# 1. not
# 2. and
# 3. or
#
# Use parentheses () when unsure.
# ============================================================

print(True or False and False)

# Evaluated as:
# True or (False and False)
# True or False
# True


# Example with Parentheses
print((True or False) and False)

# (True or False)
# True
#
# True and False
# False


# ============================================================
# SHORT-CIRCUIT EVALUATION
# ============================================================
# Python stops evaluating as soon as it knows the answer.
# ============================================================

# Example 1: AND
print(False and (10 / 0))

# Output: False
#
# No error occurs because Python sees False first.
# False and anything = False
# Therefore (10 / 0) is never executed.


# Example 2: OR
print(True or (10 / 0))

# Output: True
#
# No error occurs because Python sees True first.
# True or anything = True
# Therefore (10 / 0) is never executed.


# ============================================================
# PRACTICAL EXAMPLE 1
# ============================================================
# Check if a person can vote.
# Must be at least 18 years old.
# ============================================================

age = 20

if age >= 18:
    print("Can vote")
else:
    print("Cannot vote")


# ============================================================
# PRACTICAL EXAMPLE 2
# ============================================================
# Check if a person can enter a club.
#
# Conditions:
# - Must be 18 or older
# - Must have an invitation
# ============================================================

age = 21
has_invitation = True

if age >= 18 and has_invitation:
    print("Access granted")
else:
    print("Access denied")


# ============================================================
# PRACTICAL EXAMPLE 3
# ============================================================
# Student passes if:
# - Score >= 50
# OR
# - Has extra credit
# ============================================================

score = 45
extra_credit = True

if score >= 50 or extra_credit:
    print("Passed")
else:
    print("Failed")


# ============================================================
# PRACTICAL EXAMPLE 4
# ============================================================
# User can access the website if NOT banned.
# ============================================================

is_banned = False

if not is_banned:
    print("Access granted")
else:
    print("Access denied")


# ============================================================
# COMMON MISTAKES
# ============================================================

# WRONG
# if age >= 18 and <= 60:
#     pass

# CORRECT
age = 30

if age >= 18 and age <= 60:
    print("Valid age")


# ============================================================
# CHAIN COMPARISON
# ============================================================
# Python allows chained comparisons.
# ============================================================

age = 30

if 18 <= age <= 60:
    print("Valid age")


# ============================================================
# IMPORTANT BOOLEAN VALUES
# ============================================================
# These values are considered False:
#
# False
# None
# 0
# 0.0
# ""
# ''
# []
# {}
# ()
# set()
#
# Everything else is generally True.
# ============================================================

print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool("Hello")) # True
print(bool(10))      # True


# ============================================================
# QUICK SUMMARY
# ============================================================
#
# and
# ----
# True only when BOTH conditions are True.
#
# Example:
# age >= 18 and has_id
#
#
# or
# ---
# True when AT LEAST ONE condition is True.
#
# Example:
# is_admin or is_manager
#
#
# not
# ----
# Reverses True/False.
#
# Example:
# not is_banned
#
#
# Precedence:
# not -> and -> or
#
#
# Best Practice:
# Use parentheses when combining conditions.
#
# Example:
# (age >= 18 and has_id) or is_admin
#
# ============================================================