# ============================================================
# multiplication_table
# ============================================================
# Ask the user for a number.
# Print its multiplication table from 1 to 10.
# ============================================================

# ---------- Using a for loop ----------

number = int(input("Enter a number: "))

for i in range(1, 11):
    multiplication_table = i * number
    print(f"{number} x {i} = {multiplication_table}")


# ---------- Using a while loop ----------

number = int(input("Enter a number: "))

count = 1

while count <= 10:
    multiplication_table = number * count
    print(f"{number} x {count} = {multiplication_table}")
    count += 1