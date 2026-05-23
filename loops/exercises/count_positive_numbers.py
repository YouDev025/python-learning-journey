# count_positive_numbers
# ============================================================
# Count how many positive numbers exist (NO LISTS USED).
# ============================================================


# ---------- Using a for loop ------------
n = int(input("How many numbers would you like? :"))

positive_number = 0
for i in range(n):
    number = float(input(f"Enter a number {i+1}: "))
    if number > 0:
        positive_number += 1

print(f"You have {positive_number} positive numbers")
# ---------- Using a while loop ----------

n = int(input("How many numbers would you like? :"))
count = 0
positive_number = 0
while count < n:
    number = float(input(f"Enter a number {count+1}: "))
    if number > 0:
        positive_number += 1

    count += 1

print(f"You have {positive_number} positive numbers")
