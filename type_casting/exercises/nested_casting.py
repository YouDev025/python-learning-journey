# Convert "20.5" into float first, then convert it into int, then print result.
# A string that represents a decimal number
char = "20.5"

# Show original value (string)
print(f"The value of char is '{char}'")

# Show original type (str)
print(f"The type of char is '{type(char)}'")

# Step 1: Convert string to float
# "20.5" -> 20.5
char = float(char)

print(f"The value of char is '{char}'")
print(f"The type of char is '{type(char)}'")

# Step 2: Convert float to int
# int(20.5) removes decimal part (no rounding)
# 20.5 -> 20
char = int(char)

print(f"The value of char is '{char}'")
print(f"The type of char is '{type(char)}'")

