# ============================================================
# Ask the user for a number.
# Print:
# - Positive
# - Negative
# - Zero
# ============================================================


number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")