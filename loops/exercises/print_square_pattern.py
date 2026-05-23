# print_square_pattern
# ============================================================
# Use nested loops to print:
#
# ****
# ****
# ****
# ****
# ============================================================
print("Using a for loop ")
# ---------- Using a for   loop ------------
for i in range(4):

    for j in range(4):
        print("*",end=" ")
    print()
print("Using a while loop")
# ---------- Using a while loop ------------

i = 0
while i<4:
    j = 0
    while j<4:
         print("*",end=" ")
         j+=1

    print()
    i=i+1
