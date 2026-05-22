# ============================================
# Exercise 11: shopping_list_split
# ============================================

# Ask the user to enter 3 shopping items
# separated by commas
#
# Use split()
# Print the list

items = input("Enter items separated by a comma: ").split(",")
print(f"The items you entered are: {items}")