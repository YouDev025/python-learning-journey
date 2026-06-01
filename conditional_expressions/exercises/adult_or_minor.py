# Name: adult_or_minor
# Description:
# Ask the user for their age.
# Use a ternary operator to determine whether the user
# is an Adult or a Minor.
# ============================================================



age = int(input("What is your age? "))

is_adult = "Adult" if age >= 18 else "Minor"

print(f"You are : {is_adult}")

