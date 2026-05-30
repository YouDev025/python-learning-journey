# ============================================================
# Give the user 3 attempts to enter the correct password.
# Print:
# - Login successful
# - Account locked
# ============================================================

saved_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter your password: ")

    if password == saved_password:
        print("Login successful")
        break

    attempts += 1

if attempts == 3:
    print("Account locked")