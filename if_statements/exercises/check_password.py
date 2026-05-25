# ============================================================
# Create a saved password.
# Ask the user to enter a password.
# Print:
# - Access granted
# - Access denied
# ============================================================


password = input("Enter your password: ").lower()
if password == "password":
    print("Password is correct , access granted")
else:
    print("Password is incorrect , access denied")