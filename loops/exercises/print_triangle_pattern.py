# print_triangle_pattern
# ============================================================
# Use nested loops to print:
#
# *
# **
# ***
# ****
# *****
# ============================================================

print("# ---------- Using a for  loop ------------")

for i in range(1 , 6):
    for j in range(i):
        print("*",end=" ")
    print()
print("# ---------- Using a while loop ------------")

i = 1
while i <= 5 :
    j = 0
    while j < i:
        print("*",end=" ")
        j += 1
    print()
    i = i + 1