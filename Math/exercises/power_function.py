# Ask for base and exponent and calculate using math.pow()
import math

base = float(input("Enter a number: "))
exponent = float(input("Enter a number: "))
power = math.pow(base, exponent)
print(f"The power of {base} and {exponent} is {power}")