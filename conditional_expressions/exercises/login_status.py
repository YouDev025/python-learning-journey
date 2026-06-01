# Name: login_status
# Description:
# Ask the user if they are logged in by entering
# "yes" or "no".
# Use a ternary operator to display:
# "Logged In" or "Logged Out".
# ============================================================



logged = input("Are you logged in (yes/no): ")
login_status = "Logged in" if logged == "yes" else "logged out"

print(f"You are {login_status}")