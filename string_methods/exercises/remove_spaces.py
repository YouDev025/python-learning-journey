# ============================================================
# File Name: remove_spaces
# Description:
# Ask the user for a string and remove all spaces or (-).
# ============================================================


user_input = input("Enter a string with (-): ") #-----string-----

user_input = user_input.strip("-")

print(f"Your string without any (-) is '{user_input}'")


