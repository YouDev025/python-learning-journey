# =========================
# TYPE CASTING IN PYTHON
# =========================

# Type casting (or type conversion) is the process of converting a value from one data type to another.
# La conversion de type est le processus de transformation d'une donnée d'un type vers un autre.

# Python provides two types of type casting:
# 1. Implicit Type Casting (automatic)
# 2. Explicit Type Casting (manual)

# =========================
# 1. IMPLICIT TYPE CASTING
# =========================

# Python automatically converts one data type to another when needed.
# This is done to prevent data loss.

# Example:
x = 5        # int
y = 2.5      # float

result = x + y  # int is automatically converted to float
# result = 7.5 (float)

# =========================
# RULE:
# Python converts smaller data types to larger data types automatically:
# int → float → complex

# Example:
a = 10       # int
b = 3.0      # float
c = a + b    # result is float

# =========================
# 2. EXPLICIT TYPE CASTING
# =========================

# Explicit type casting is when the programmer manually converts one type into another.

# =========================
# COMMON TYPE CASTING FUNCTIONS
# =========================

# int()    → converts to integer
# float()  → converts to float
# str()    → converts to string
# bool()   → converts to boolean

# =========================
# int() EXAMPLE
# =========================

num = "100"          # string
num_int = int(num)   # converted to integer

# =========================
# float() EXAMPLE
# =========================

num2 = "3.14"
num_float = float(num2)

# =========================
# str() EXAMPLE
# =========================

age = 25
age_str = str(age)

# =========================
# bool() EXAMPLE
# =========================

# False values in Python:
# 0, 0.0, "", None, [], {}, ()

x = 0
x_bool = bool(x)  # False

y = 10
y_bool = bool(y)  # True

# =========================
# IMPORTANT NOTES
# =========================

# - Converting incompatible values will cause errors:
# int("hello") → ERROR

# - Type casting does NOT change the original variable unless reassigned:
# x = "10"
# x = int(x)  # now x is integer

# =========================
# END OF TYPE CASTING NOTES
# =========================