# guess_the_secret_number
# ============================================================
# Create a guessing game.
#
# Secret number = 7
#
# Keep asking the user until they guess correctly.
# Use while loop.
# ============================================================

# ---------- Using a for loop ------------
secret_number = 7
max_attempts = 3
found = False
for i in range(max_attempts):
    gess = int(input(f"Attempt {i+1} -Gesse the secret number? : "))
    if gess == secret_number:
        print("Congratulations! You got it right!")
        found = True
        break
    else:
        print(f"Sorry, you have {gess} attempts to guess the secret number.")

if not found:
    print(f"Game over! The secret number was {secret_number}")

# ---------- Using a while loop ----------

secret_number = 7
gess = int(input("Guess the secret number? : "))
while gess != secret_number:
    print(f"Sorry, Wrong guess , try again")
    gess = int(input("Guess the secret number? : "))

print(f"Congratulations! You got it right!")