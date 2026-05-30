# ============================================================
# Ask the user for a number.
# Check if it is between 1 and 100.
# ============================================================

 
number = float(input("Enter a number: "))

if 1 <= number <= 100:
    print(f"{number} is in range 1 to 100")
else:
    print(f"{number} is out of range")