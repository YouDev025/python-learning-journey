# Extract only letters from a string.



user_input = input("Enter your string :" )

alpha = ""

for char in user_input:
    if char.isalpha():
        alpha += char

if alpha == "":
    print("Your string is empty")
else:
    print(alpha)