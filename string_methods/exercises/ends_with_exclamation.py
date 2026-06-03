# Check if a string ends with "!".


user_input = input("Enter a string: ")

if user_input != "":
    last_char = user_input[-1].lower()
    if last_char == "!":
        print("Your string ends with a exclamation point '!'")
    else:
        print("Your string does not end with a exclamation point '!'")

else:
    print("Error : empty string")