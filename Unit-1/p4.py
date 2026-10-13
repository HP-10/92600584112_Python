name = input("Enter your name: ")
city = input("Enter your city: ")

print("\n========== STRING ==========")

# Full string
print("Name:", name)

# String slicing
print("First 3 characters:", name[0:3])

# String formatting
print("\n========== STRING FORMATTING ==========")
print("My name is {} and I live in {}.".format(name, city))

print(f"My name is {name} and I live in {city}.")


# Built-in String Functions
print("\n========== STRING FUNCTIONS ==========")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Length:", len(name))
print("Replace:", name.replace("a", "A"))
print("Count of 'a':", name.count("a"))
