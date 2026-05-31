# ============================================================
# Print True if role is:
# - "admin"
# OR
# - "manager"
#
# Example:
# role = "manager"
# Output:
# True
# ============================================================


user_role = input("Your role: ")
role = (user_role == "admin") or (user_role == "manager")
if role:
    print(role)
else:
    print(role)

