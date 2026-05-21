# a = "9"
# b = "2"
# Convert both to int and divide a / b, then print result.

# a and b are strings containing numeric values
a = "9"
b = "2"

# Convert string to integer
# "9" -> 9
a = int(a)
print(f"The new a is {a}")

# Convert string to integer
# "2" -> 2
b = int(b)
print(f"The new b is {b}")

# Perform normal division
# Note: / always returns a float in Python
d = a / b

# Print final result
print(f"The division of {a} by {b} is {d}")