# ============================================================
# Ask the user for a score.
# Print:
# A -> 90+
# B -> 80+
# C -> 70+
# D -> 50+
# F -> below 50
# ============================================================



score = float(input("Enter your score: "))

if score >= 90:
    print(f"Your grade is A")
elif score >= 80:
    print(f"Your grade is B")
elif score >= 70:
    print(f"Your grade is C")
elif score >= 50:
    print(f"Your grade is D")
else:
    print(f"Your grade is F")
