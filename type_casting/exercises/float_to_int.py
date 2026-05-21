# Convert the float 9.99 into an integer and print the result.


my_float = 9.99
print(f"The Float is {my_float} before type casting")
my_int = int(my_float)
print(f"The Int is {my_int} after type casting")

# (Check what happens to the decimal part)
# int() removes the decimal part (truncation, not rounding)
int(9.99)  # 9
int(9.1)   # 9
int(-9.99) # -9