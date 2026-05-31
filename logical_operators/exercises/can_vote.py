# ============================================================
# Check if a person can vote.
# A person can vote if they are 18 or older.
# ============================================================

age = int(input("What is your age? "))
can_vote = age >= 18
if can_vote:
    print("You can vote.")
else:
    print("You cannot vote.")