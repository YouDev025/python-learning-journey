# reverse_a_string
# ============================================================
# Ask the user for a word.
# Reverse the word using a loop.
# ============================================================

# ---------- Using a for loop ----------

word = input("Enter a word: ") #HELLO
reversed_word = "H" #-->OLLEH
for letter in word:
    reversed_word = letter + reversed_word

print(f"The reverse of '{word}' is '{reversed_word}'")


# ---------- Using a while loop ----------

word = input("Enter a word: ")
reversed_word = ""
index = len(word) - 1
while index >= 0:
    reversed_word += word[index]
    index -= 1

print(f"The reverse of '{word}' is '{reversed_word}'")