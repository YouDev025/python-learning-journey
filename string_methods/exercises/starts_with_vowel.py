# Check if a string starts with a vowel.


user_input = input("Enter a string: ")

if user_input != "":
    first_letter = user_input[0].lower()

    if first_letter in ["a", "e", "i", "o", "u"]:
        print("Your string starts with a vowel")
    else:
        print("Your string does not start with a vowel")
else:
    print("Your entered a empty string")