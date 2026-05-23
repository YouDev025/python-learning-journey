# find_largest_number
# ============================================================
# Ask the user for several numbers one by one.
# Find and print the largest number (NO LISTS USED).
# ============================================================


n = int(input("How many numbers would you like? :"))
largest_number = None

# ---------- Using a for loop ----------

for i in range(n):
    number = float(input(f"Enter a number {i+1}: "))
    if largest_number is None or number > largest_number:
        largest_number = number

print(f"The largest number is {largest_number}")

# ---------- Using a while loop ----------
n = int(input("How many numbers do you want to enter? :"))

count = 0
largest = None
while count < n:
    number = float(input(f"Enter a number {count+1}: "))
    if largest is None or number > largest:
        largest = number

    count += 1

print(f"The largest number is {largest}")