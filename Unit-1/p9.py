# Program to define and use user-defined functions
# with different types of arguments


# 1. Function without arguments
def welcome():
    print("Welcome to Marwadi University.")


print("========== FUNCTION WITHOUT ARGUMENTS ==========")
welcome()


# 2. Function with positional arguments
def addition(num1, num2):
    print("Addition:", num1 + num2)


print("\n========== POSITIONAL ARGUMENTS ==========")
addition(20, 30)


# 3. Function with keyword arguments
print("\n========== KEYWORD ARGUMENTS ==========")
addition(num2=10, num1=15)


# 4. Function with default argument
def student(name, course="MCA"):
    print("Name:", name)
    print("Course:", course)


print("\n========== DEFAULT ARGUMENT ==========")
student("Harsh")
student("Jenish", "BCA")


# 5. Function with variable-length arguments
def user(*name):
    print("Users:", name)


print("\n========== VARIABLE-LENGTH ARGUMENTS ==========")
user("HP")
user("Jenish", "Pranav", "Harsh")