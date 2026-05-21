# Exercise 5: variable_swapper_challenge

# Create variables:
# x = 15
# y = 30

# Swap their values without using a third variable

# Print x and y

# ANSWER

x = 15
y = 30
print(f"The old x value is {x} and the old y value is {y}")

x, y = y, x
print(f"The new x is {x} and the new y is {y}")