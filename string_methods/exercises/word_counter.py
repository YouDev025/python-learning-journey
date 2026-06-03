# ============================================================
# File Name: count_words
# Description:
# Ask the user for a sentence and count how many words it contains.
# ============================================================

# Ask the user to enter a sentence
user_input = input("Enter a string: ")

# Initialize the word counter
word_counter = 0

# Loop through each word in the sentence
for word in user_input.split():
    word_counter += 1

# Display the result
print(f"Your string has {word_counter} words.")