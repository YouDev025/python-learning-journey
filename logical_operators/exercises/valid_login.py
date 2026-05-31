# ============================================================
# Username must be "admin"
# Password must be "1234"
#
# Example:
# username = "admin"
# password = "1234"
# Output:
# True
# ============================================================


saved_username = "admin"
saved_password = "1234"

username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == saved_username and password == saved_password:
    print("Login Successful")
else:
    print("Login Unsuccessful")

