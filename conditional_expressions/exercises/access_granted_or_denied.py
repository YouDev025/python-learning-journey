# Name: access_granted_or_denied
# Description:
# Create a username variable containing "admin".
# Ask the user for a username.
# Use a ternary operator to determine whether access
# should be Granted or Denied.
# ============================================================



saved_username = "admin"
saved_password = "1234"

username = input("Enter your username: ")
password = input("Enter your password: ")

is_granted = "Access granted" if username == saved_username and password == saved_password else "Access denied"


print(is_granted)