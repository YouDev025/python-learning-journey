# ============================================
# Exercise 19: number_guess_loop
# ============================================

# Create a secret number = 7
#
# Ask the user to guess the number
#
# Keep asking until the user guesses correctly
#
# Print:
# "Correct!"

secret_number = 7

guess = int(input("Please enter your guess: "))
if guess == secret_number:
    print("You guessed the number")
else:
    print("Try again")