# ============================================================
# A student passes if:
# - score >= 50
# AND
# - attendance >= 75
#
# Example:
# score = 70
# attendance = 80
# Output:
# True
# ============================================================




score = int(input("Please enter your score: "))
attendance = int(input("Please enter your attendance: "))

pass_exam = (score >= 50) and (attendance >= 75)


if pass_exam:
    print("You have passed the exam")
else:
    print("You have not passed the exam")