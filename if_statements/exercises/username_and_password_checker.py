# ============================================================
# Create:
# - saved username
# - saved password
#
# Ask the user to enter both.
# Check if both are correct.
# ============================================================


saved_user_name = "user123"
saved_password = "python123"

user_name = input("Enter a username: ")
password = input("Enter a password: ")
if user_name == saved_user_name and password == saved_password:
    print("You are logged in")
else:
    print("username or password is incorrect")

