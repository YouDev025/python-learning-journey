# ============================================
# Exercise 20: student_information_system
# ============================================

# Ask the user for:
# student name
# student age
# favorite programming language
# average grade
#
# Print all information using f-string
#
# Example:
# Name: Yassine
# Age: 20
# Language: Python
# Average: 16.5


student_name = input("student name: ").strip()
student_age = input("student age: ").strip()
programming_language = input("favorite programming language: ").strip()
average_grade =input("average grade: ").strip()

print(f"The student name is {student_name}")
print(f"The student age is {student_age}")
print(f"The programming language is {programming_language}")
print(f"The average grade is {average_grade}")
