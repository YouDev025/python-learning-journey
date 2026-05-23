# ============================================================
# count_vowels_in_word
# ============================================================
# Ask the user for a word.
# Count how many vowels it contains.
# ============================================================


# ---------- Using a for loop ----------

# Ask the user to enter a word
word = input("Enter a word: ").lower()

# Variable to store the number of vowels
count = 0

# Loop through every letter in the word
for letter in word:

    # Check if the letter is a vowel
    if letter in "aeiou":
        count += 1

# Display the result
print(f"There are {count} vowels in '{word}'")


# ---------- Using a while loop ----------

# Ask the user to enter another word
word = input("Enter a word: ").lower()

# Variable to count vowels
count = 0

# Start index at 0
index = 0

# Continue while index is inside the word length
while index < len(word):

    # Check if the current letter is a vowel
    if word[index] in "aeiou":
        count += 1

    # Move to the next letter
    index += 1

# Display the result
print(f"There are {count} vowels in '{word}'")