# ============================================================
# Ask the user for a number.
# Check if the number is divisible by:
# - both 3 and 5
# - only 3
# - only 5
# - neither
# ============================================================

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"The number {number} is divisible by both 3 and 5")

elif number % 3 == 0:
    print(f"The number {number} is divisible only by 3")

elif number % 5 == 0:
    print(f"The number {number} is divisible only by 5")

else:
    print(f"The number {number} is divisible by neither 3 nor 5")