# ============================================================
# A customer gets a discount if:
# - age >= 60
# OR
# - is_student is True
#
# Example:
# age = 25
# is_student = True
# Output:
# True
# =========================================================


age = int(input("Please enter your age: "))
student = input("Are you a student? y/n: ")


eligible_for_discount = (age >= 60) or (student == "y")

if eligible_for_discount :
    print("You are eligible for discount")
else:
    print("You are not eligible for discount")





