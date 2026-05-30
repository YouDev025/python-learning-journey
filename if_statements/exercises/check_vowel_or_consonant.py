# ============================================================
# Ask the user for a letter.
# Check if it is:
# - vowel
# - consonant
# ============================================================


letter = input("Enter a letter: ")
if letter in "aeiou":
    print("You entered a vowel")
else:
    print("You entered a consonant")