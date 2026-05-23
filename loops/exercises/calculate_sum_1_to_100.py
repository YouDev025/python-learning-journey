# ============================================================
# calculate_sum_1_to_100
# ============================================================
# Calculate and print the sum of numbers from 1 to 100.
# ============================================================

# ---------- Using a for loop ----------

total = 0

for count in range(1, 101): # range(1, 100) stops at 99, not 100.
    total += count

print(f"The sum using for loop is: {total}")


# ---------- Using a while loop ----------

total = 0
count = 1

while count <= 100:
    total += count
    count += 1

print(f"The sum using while loop is: {total}")