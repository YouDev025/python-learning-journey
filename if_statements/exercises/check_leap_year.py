# ============================================================
# Ask the user for a year.
# Check if it is a leap year.
# ============================================================

year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} Leap year")
else:
    print(f"{year} Not a leap year")