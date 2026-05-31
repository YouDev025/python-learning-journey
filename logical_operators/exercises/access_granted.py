# ============================================================
# A user can enter if:
# - age >= 18
# - has_id is True
#
# Example:
# age = 22
# has_id = True
# Output:
# True
# ============================================================


age = int(input("What is your age? "))
has_id = input("Do you have an ID? (y/n) ").lower()

can_enter = age >= 18 and has_id == "y"

if can_enter:
    print("Access granted")
else:
    print("Access denied")