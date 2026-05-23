# stop_loop_using_break
# ============================================================
# Print numbers from 1 to 20.
# Stop the loop when the number becomes 13.
# ============================================================


# ---------- Using a for loop --------------

for number in range(1,21):
    if number == 13 :
        break
    else:
        print(number)

# ---------- Using a while loop ------------
count = 1
while count <=20:
    if count == 13:
        break

    print(count)
    count = count + 1