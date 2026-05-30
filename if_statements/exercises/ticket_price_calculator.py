# ============================================================
# Ask the user for their age.
#
# Ticket prices:
# - Under 12 -> 10$
# - 12 to 18 -> 15$
# - Adults -> 20$
# ============================================================


age = int(input("Enter your age: "))
if age < 12:
    print("The price of your ticket is 10$")
elif 12 <= age <= 18:
    print("The price of your ticket is 15$")
else:
    print("The price of your ticket is 20$")