# Name: pass_or_fail
# Description:
# Ask the user for a score.
# Use a ternary operator to determine whether the student
# Passes or Fails.
# A score of 50 or higher is considered a Pass.
# ============================================================



score = float(input("Enter your score: "))
is_passed = "Passed" if score >= 50 else "Failed"

print(f"Your score is {score} and you {is_passed}")