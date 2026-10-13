# Global variable
university = "Marwadi University"


# Function to demonstrate local variable
def local_example():
    course = "MCA"
    print("Local Variable:", course)


# Calling the function
local_example()

# Accessing the global variable
print("Global Variable:", university)


# Function to demonstrate nonlocal variable
def outer_function():

    message = "Welcome to Marwadi University."

    def inner_function():
        nonlocal message
        message = "Welcome to the Department of Computer Applications."

    inner_function()
    return message


# Calling the outer function
print("Nonlocal Variable:", outer_function())