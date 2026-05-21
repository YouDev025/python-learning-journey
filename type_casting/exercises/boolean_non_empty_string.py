# Convert the string "Hello" into a boolean and print the result.

non_empty_string = "this is a test"
print(f"The non-empty string is '{non_empty_string}' and type is {type(non_empty_string)}")

boolean_string =bool(non_empty_string)
print(f"The boolean string is '{boolean_string}' and type is {type(boolean_string)}")

#In Python:

bool("") #→ False (empty string)
bool("Hello") # → True (non-empty string)
bool("anything") # → True

#Example:

bool("")        # False
bool("Hello")   # True
bool("0")       # True (still a non-empty string!)