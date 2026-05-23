# ============================================================
# PYTHON LOOPS - COMPLETE BEGINNER TO INTERMEDIATE GUIDE
# ============================================================
# This file contains:
# 1. while loops
# 2. for loops
# 3. range()
# 4. break
# 5. continue
# 6. pass
# 7. nested loops
# 8. loop else
# 9. practical examples
# 10. common mistakes
# 11. useful notes and tips
#
# Every explanation is written as comments.
# Uncomment sections one by one to practice.
# ============================================================


# ============================================================
# 1. WHAT IS A LOOP?
# ============================================================
# A loop is used to repeat code multiple times.
#
# Python has two main loops:
# - while loop
# - for loop
#
# Use loops when:
# - Repeating tasks
# - Working with lists
# - Counting
# - Processing data
# - Asking user input repeatedly
# ============================================================


# ============================================================
# 2. WHILE LOOP
# ============================================================
# Syntax:
# while condition:
#     code
#
# The loop continues WHILE the condition is True.
# ============================================================

# Example 1: Simple while loop

# count = 1
#
# while count <= 5:
#     print(count)
#     count += 1
#
# Output:
# 1
# 2
# 3
# 4
# 5


# ------------------------------------------------------------
# IMPORTANT NOTE:
# count += 1 means:
# count = count + 1
#
# If you forget to update the variable,
# the loop may become an infinite loop.
# ------------------------------------------------------------


# Example 2: Infinite loop

# while True:
#     print("This runs forever")

# To stop an infinite loop manually:
# Press CTRL + C in terminal.


# Example 3: Countdown

# number = 5
#
# while number > 0:
#     print(number)
#     number -= 1
#
# print("Finished!")


# ============================================================
# 3. FOR LOOP
# ============================================================
# A for loop is used to iterate over sequences.
#
# Sequences include:
# - lists
# - strings
# - tuples
# - ranges
# ============================================================


# Example 1: Loop through a list

# fruits = ["apple", "banana", "orange"]
#
# for fruit in fruits:
#     print(fruit)


# Example 2: Loop through a string

# word = "Python"
#
# for letter in word:
#     print(letter)


# ------------------------------------------------------------
# IMPORTANT NOTE:
# The variable inside the loop changes automatically.
# Example:
# for fruit in fruits:
#
# fruit becomes:
# - apple
# - banana
# - orange
# one by one.
# ------------------------------------------------------------


# ============================================================
# 4. range() FUNCTION
# ============================================================
# range() generates numbers.
#
# Commonly used with for loops.
# ============================================================


# Example 1: range(stop)

# for number in range(5):
#     print(number)

# Output:
# 0
# 1
# 2
# 3
# 4


# ------------------------------------------------------------
# IMPORTANT NOTE:
# range(5) starts from 0 by default.
# It stops BEFORE 5.
# ------------------------------------------------------------


# Example 2: range(start, stop)

# for number in range(1, 6):
#     print(number)

# Output:
# 1 2 3 4 5


# Example 3: range(start, stop, step)

# for number in range(0, 11, 2):
#     print(number)

# Output:
# 0 2 4 6 8 10


# Example 4: Negative step

# for number in range(10, 0, -1):
#     print(number)

# Output:
# 10 9 8 7 6 5 4 3 2 1


# ============================================================
# 5. break STATEMENT
# ============================================================
# break immediately stops the loop.
# ============================================================


# Example:

# for number in range(1, 11):
#
#     if number == 5:
#         break
#
#     print(number)

# Output:
# 1 2 3 4


# ------------------------------------------------------------
# IMPORTANT NOTE:
# When break happens:
# - The loop ends completely.
# - Remaining iterations are skipped.
# ------------------------------------------------------------


# ============================================================
# 6. continue STATEMENT
# ============================================================
# continue skips the CURRENT iteration.
# The loop continues normally afterward.
# ============================================================


# Example:

# for number in range(1, 6):
#
#     if number == 3:
#         continue
#
#     print(number)

# Output:
# 1 2 4 5


# ------------------------------------------------------------
# IMPORTANT NOTE:
# continue does NOT stop the loop.
# It only skips one iteration.
# ------------------------------------------------------------


# ============================================================
# 7. pass STATEMENT
# ============================================================
# pass does nothing.
#
# It is used as a placeholder.
# ============================================================


# Example:

# for number in range(5):
#     pass

# Useful when writing code later.


# ============================================================
# 8. NESTED LOOPS
# ============================================================
# A loop inside another loop.
# ============================================================


# Example 1: Basic nested loop

# for i in range(3):
#
#     for j in range(2):
#         print("i =", i, "j =", j)


# ------------------------------------------------------------
# IMPORTANT NOTE:
# The inner loop runs completely
# for every single iteration of the outer loop.
# ------------------------------------------------------------


# Example 2: Multiplication table

# for i in range(1, 6):
#
#     for j in range(1, 6):
#         print(i * j, end="\t")
#
#     print()


# ============================================================
# 9. LOOPING THROUGH LISTS
# ============================================================


# Example 1: Access items

# numbers = [10, 20, 30, 40]
#
# for number in numbers:
#     print(number)


# Example 2: Using index

# numbers = [10, 20, 30]
#
# for index in range(len(numbers)):
#     print(index, numbers[index])


# ------------------------------------------------------------
# IMPORTANT NOTE:
# len(list) returns the number of items.
# ------------------------------------------------------------


# ============================================================
# 10. enumerate()
# ============================================================
# enumerate() gives:
# - index
# - value
# together.
# ============================================================


# Example:

# fruits = ["apple", "banana", "orange"]
#
# for index, fruit in enumerate(fruits):
#     print(index, fruit)


# Output:
# 0 apple
# 1 banana
# 2 orange


# ============================================================
# 11. LOOPING THROUGH DICTIONARIES
# ============================================================


# Example:

# student = {
#     "name": "Ali",
#     "age": 21,
#     "city": "Marrakech"
# }
#
# for key, value in student.items():
#     print(key, value)


# ============================================================
# 12. LOOP ELSE
# ============================================================
# Loops can have an else block.
#
# The else runs when:
# - the loop finishes normally
#
# The else does NOT run if break happens.
# ============================================================


# Example 1: for else

# for number in range(5):
#     print(number)
# else:
#     print("Loop finished normally")


# Example 2: break prevents else

# for number in range(5):
#
#     if number == 3:
#         break
#
#     print(number)
# else:
#     print("This will not print")


# ============================================================
# 13. PRACTICAL EXAMPLES
# ============================================================


# ------------------------------------------------------------
# Example 1: Sum numbers
# ------------------------------------------------------------

# total = 0
#
# for number in range(1, 6):
#     total += number
#
# print("Total =", total)


# ------------------------------------------------------------
# Example 2: Find even numbers
# ------------------------------------------------------------

# for number in range(1, 21):
#
#     if number % 2 == 0:
#         print(number)


# ------------------------------------------------------------
# IMPORTANT NOTE:
# % is modulus operator.
# It gives the remainder.
#
# Example:
# 10 % 2 = 0
# 7 % 2 = 1
# ------------------------------------------------------------


# ------------------------------------------------------------
# Example 3: User input loop
# ------------------------------------------------------------

# while True:
#
#     password = input("Enter password: ")
#
#     if password == "python123":
#         print("Access granted")
#         break
#
#     print("Wrong password")


# ------------------------------------------------------------
# Example 4: Count vowels
# ------------------------------------------------------------

# text = "programming"
# vowels = "aeiou"
# count = 0
#
# for letter in text:
#
#     if letter in vowels:
#         count += 1
#
# print("Vowels:", count)


# ------------------------------------------------------------
# Example 5: Reverse string
# ------------------------------------------------------------

# word = "Python"
# reversed_word = ""
#
# for letter in word:
#     reversed_word = letter + reversed_word
#
# print(reversed_word)


# ============================================================
# 14. COMMON LOOP MISTAKES
# ============================================================


# ------------------------------------------------------------
# Mistake 1: Infinite loops
# ------------------------------------------------------------

# WRONG:
# count = 1
#
# while count <= 5:
#     print(count)
#
# count never changes.


# ------------------------------------------------------------
# Mistake 2: Wrong indentation
# ------------------------------------------------------------

# WRONG:
# for i in range(5):
# print(i)
#
# Python requires indentation.


# ------------------------------------------------------------
# Mistake 3: Off-by-one errors
# ------------------------------------------------------------

# range(5) gives:
# 0 1 2 3 4
#
# NOT 0 1 2 3 4 5


# ============================================================
# 15. USEFUL LOOP PATTERNS
# ============================================================


# ------------------------------------------------------------
# Pattern 1: Counter
# ------------------------------------------------------------

# count = 0
#
# for letter in "Python":
#     count += 1
#
# print(count)


# ------------------------------------------------------------
# Pattern 2: Accumulator
# ------------------------------------------------------------

# total = 0
#
# for number in range(1, 6):
#     total += number
#
# print(total)


# ------------------------------------------------------------
# Pattern 3: Search
# ------------------------------------------------------------

# numbers = [4, 8, 2, 9, 1]
# target = 9
# found = False
#
# for number in numbers:
#
#     if number == target:
#         found = True
#         break
#
# print(found)


# ============================================================
# 16. LIST COMPREHENSION (BONUS)
# ============================================================
# Short way to create lists.
# ============================================================


# Example:

# squares = [number ** 2 for number in range(1, 6)]
#
# print(squares)

# Output:
# [1, 4, 9, 16, 25]


# ============================================================
# 17. QUICK SUMMARY
# ============================================================
# while loop:
# - Runs while condition is True
# - Good when number of repetitions is unknown
#
# for loop:
# - Iterates through sequences
# - Good for lists, strings, ranges
#
# break:
# - Stops loop completely
#
# continue:
# - Skips current iteration
#
# pass:
# - Placeholder that does nothing
#
# nested loop:
# - Loop inside another loop
# ============================================================
# ============================================================
# END OF FILE
# ============================================================
# Best way to learn loops:
# 1. Read examples
# 2. Uncomment code
# 3. Run it
# 4. Modify it
# 5. Practice daily
# ============================================================
