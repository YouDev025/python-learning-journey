# skip_number_using_continue
# ============================================================
# Print numbers from 1 to 10.
# Skip number 5 using continue.
# ============================================================

# ---------- Using a for loop ------------

for number in range (1 , 11):
    if number == 5:
        continue
    else:
        #pass
        print(number)

# ---------- Using a while loop ------------

print("#"*50)
count = 1

while count <= 10:

    if count == 5:
        count += 1
        continue

    print(count)
    count += 1


