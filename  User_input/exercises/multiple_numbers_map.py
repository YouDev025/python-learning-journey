
# ============================================
# Exercise 12: multiple_numbers_map
# ============================================

# Ask the user to enter two numbers
# in one line separated by space
#
# Use map() and int()
# Print the sum
number1 , number2 = map(int, input("Enter two numbers separated by space: ").split())
total = number1 + number2
print(f" The sum of {number1} and {number2} is: {total}")

