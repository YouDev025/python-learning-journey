# ============================================================
# File Name: find_longest_word_no_list
# Description:
# Find the longest word in a sentence WITHOUT using lists.
# ============================================================

user_input = input("Enter a sentence: ")

current_word = ""
longest_word = ""

for char in user_input:
    if char != " ":
        # build the current word
        current_word += char
    else:
        # space = word finished, compare lengths
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ""

# check last word
if len(current_word) > len(longest_word):
    longest_word = current_word

print(f"The longest word is: '{longest_word}'")
print(f"It has {len(longest_word)} characters.")