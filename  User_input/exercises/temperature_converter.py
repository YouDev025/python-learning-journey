# ============================================
# Exercise 16: temperature_converter
# ============================================

# Ask the user for temperature in Celsius
#
# Convert it to Fahrenheit
#
# Formula:
# Fahrenheit = (Celsius * 9/5) + 32
#
# Print the result


temp_cels =float(input("Enter the temperature in celsius : "))
fahrenheit = (temp_cels * 9/5) + 32
print(f"The temperature in celsius is: {temp_cels}C")
print(f"The temperature in fahrenheit is {fahrenheit}F")
