
# ============================================
# Exercise 18: login_system
# ============================================

# Ask the user for:
# username
# password
#
# If username == "admin"
# and password == "1234"
#
# print "Login successful"
#
# otherwise print "Invalid credentials"


username = input("Please enter your username: ").strip()
password = input("Please enter your password: ").strip()

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid credentials")