# Program to create a dictionary and demonstrate
# dictionary methods and iteration

user_info = {}

# Taking input from user
user_name = input("Enter the name of user: ")
user_age = int(input("Enter age of user: "))
user_city = input("Enter the city of user: ")

# Adding data to dictionary
user_info['Name'] = user_name
user_info['Age'] = user_age
user_info['City'] = user_city

print("\n========== DICTIONARY ==========")
print("Full Dictionary:", user_info)

# Dictionary keys
print("\nKeys:", user_info.keys())

# Dictionary values
print("Values:", user_info.values())

# Dictionary items
print("Items:", user_info.items())

# Get method
print("Name using get():", user_info.get('Name'))

# Dictionary iteration
print("\n========== ITERATION ==========")
for key, value in user_info.items():
    print(key, ":", value)

# Pop method
print("\nRemoved value:", user_info.pop('Name'))
print("After pop:", user_info)

# Clear method
user_info.clear()
print("After clear:", user_info)
