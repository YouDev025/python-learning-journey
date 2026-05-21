# ============================================
# VARIABLES IN PYTHON
# ============================================

# EN:
# A variable is a named container used to store data in a program.

# FR:
# Une variable est un espace nommé utilisé pour stocker des données.


# ============================================
# 1. Creating Variables
# ============================================

name = "Yassine"
age = 20
height = 1.75
is_student = True

print(name, age, height, is_student)


# ============================================
# 2. Changing Variable Value
# ============================================

age = 21
print("Updated age:", age)


# ============================================
# 3. Python Automatically Detects Types
# ============================================

x = 10
y = "Hello"

print(type(x))
print(type(y))


# ============================================
# 4. Main Variable Types
# ============================================

age = 20               # int
height = 1.75          # float
name = "Yassine"       # str
is_student = True      # bool

colors = ["red", "blue"]     # list
coords = (10, 20)            # tuple
student = {"name": "Ali"}    # dict
numbers = {1, 2, 3}          # set
data = None                  # NoneType
z = 2 + 3j                  # complex


# ============================================
# 5. TYPE CONVERSION (CASTING)
# ============================================

# --- int() -> convert to integer
a = int(3.7)        # 3
b = int("10")       # 10

# --- float() -> convert to float
c = float(5)        # 5.0
d = float("2.5")    # 2.5

# --- str() -> convert to string
e = str(100)        # "100"
f = str(3.14)       # "3.14"

# --- bool() -> convert to boolean
g = bool(1)         # True
h = bool(0)         # False
i = bool("")        # False

# --- list() -> convert to list
j = list("abc")     # ['a', 'b', 'c']
k = list((1, 2))    # [1, 2]

# --- tuple() -> convert to tuple
l = tuple([1, 2, 3])  # (1, 2, 3)

# --- set() -> convert to set (removes duplicates)
m = set([1, 1, 2, 3])  # {1, 2, 3}


# ============================================
# 6. Examples of Conversions in Practice
# ============================================

num_str = "50"

num_int = int(num_str)     # string -> int
num_float = float(num_str) # string -> float

print(num_int + 10)        # 60
print(num_float + 2.5)     # 52.5