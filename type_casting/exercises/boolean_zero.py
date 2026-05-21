# Convert the number 0 into a boolean and print the result.
# Convert number 0 to boolean
number = 0
print(f"The number is {number} and type is {type(number)}")

# bool(0) -> False (because 0 is considered False in Python)
my_bool = bool(number)
print(f"The bool is {my_bool} and type is {type(my_bool)}")


# Convert number 1 to boolean
number2 = 1
print(f"The number is {number2} and type is {type(number2)}")

# bool(1) -> True (any non-zero number is True)
my_bool2 = bool(number2)
print(f"The bool is {my_bool2} and type is {type(my_bool2)}")


# Convert a positive number to boolean
number3 = 100
print(f"The number is {number3} and type is {type(number3)}")

# Any non-zero value is True
my_bool3 = bool(number3)
print(f"The bool is {my_bool3} and type is {type(my_bool3)}")


# Convert a negative number to boolean
number4 = -5
print(f"The number is {number4} and type is {type(number4)}")

# Any non-zero value (even negative) is True
my_bool4 = bool(number4)
print(f"The bool is {my_bool4} and type is {type(my_bool4)}")