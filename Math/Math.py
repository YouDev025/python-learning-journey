# ============================================
# Math.py - Python Math Essentials (with Definitions + Outputs)
# ============================================

# ============================================
# 1. BASIC ARITHMETIC OPERATORS
# ============================================

a = 10
b = 3

print("Addition (+):", a + b)
# OUTPUT: 13

print("Subtraction (-):", a - b)
# OUTPUT: 7

print("Multiplication (*):", a * b)
# OUTPUT: 30

print("Division (/):", a / b)
# OUTPUT: 3.3333333333333335

print("Floor Division (//):", a // b)
# OUTPUT: 3

print("Modulus (%):", a % b)
# OUTPUT: 1

print("Power (**):", a ** b)
# OUTPUT: 1000


# ============================================
# 2. BUILT-IN MATH FUNCTIONS
# ============================================

print("abs(-10):", abs(-10))
# OUTPUT: 10

print("round(3.6):", round(3.6))
# OUTPUT: 4

print("min(1,5,9):", min(1,5,9))
# OUTPUT: 1

print("max(1,5,9):", max(1,5,9))
# OUTPUT: 9

print("pow(2,3):", pow(2,3))
# OUTPUT: 8


# ============================================
# 3. MATH MODULE
# ============================================

import math

print("sqrt(16):", math.sqrt(16))
# OUTPUT: 4.0

print("ceil(4.2):", math.ceil(4.2))
# OUTPUT: 5

print("floor(4.9):", math.floor(4.9))
# OUTPUT: 4

print("pi:", math.pi)
# OUTPUT: 3.141592653589793

print("e:", math.e)
# OUTPUT: 2.718281828459045

print("factorial(5):", math.factorial(5))
# OUTPUT: 120

print("log(10):", math.log(10))
# OUTPUT: 2.302585092994046


# ============================================
# 4. TRIGONOMETRY
# ============================================

angle = math.radians(90)

print("sin(90°):", math.sin(angle))
# OUTPUT: 1.0 (approximately)

print("cos(90°):", math.cos(angle))
# OUTPUT: 6.123233995736766e-17 (≈ 0)

print("tan(45°):", math.tan(math.radians(45)))
# OUTPUT: 0.9999999999999999 (≈ 1)


# ============================================
# 5. RANDOM NUMBERS
# ============================================

import random

print("random():", random.random())
# OUTPUT: (random number like 0.2345, changes every run)

print("randint(1,10):", random.randint(1,10))
# OUTPUT: (random integer between 1 and 10)

items = [10, 20, 30]
print("choice:", random.choice(items))
# OUTPUT: (10 or 20 or 30 randomly)


# ============================================
# 6. TYPE CONVERSION
# ============================================

x = 5.8

print("int(x):", int(x))
# OUTPUT: 5

print("float(5):", float(5))
# OUTPUT: 5.0

print("str(100):", str(100))
# OUTPUT: "100"


# ============================================
# 7. EVEN / ODD CHECK
# ============================================

num = 7

if num % 2 == 0:
    print(num, "is Even")
    # OUTPUT (if even): 7 is Even
else:
    print(num, "is Odd")
    # OUTPUT: 7 is Odd


# ============================================
# 8. SIMPLE FUNCTIONS
# ============================================

def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        return "Error: division by zero"
    return x / y

print("add:", add(5, 3))
# OUTPUT: 8

print("divide:", divide(10, 2))
# OUTPUT: 5.0


# ============================================
# END OF FILE
# ============================================