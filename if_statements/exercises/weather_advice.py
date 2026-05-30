# ============================================================
# Ask the user for the weather:
# - sunny
# - rainy
# - snowy
#
# Print suitable advice.
# ============================================================
weather = input("Enter the weather (sunny, rainy, snowy): ").lower()

if weather == "sunny":
    print("Wear sunglasses and stay hydrated.")

elif weather == "rainy":
    print("Take an umbrella.")

elif weather == "snowy":
    print("Wear a warm coat and boots.")

else:
    print("Weather not recognized.")