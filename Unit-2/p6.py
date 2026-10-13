# List
numbers = [10, 20, 30, 40, 50, 60]

# String
text = "Marwadi University"

# Dictionary
student = {
    "Name": "Harsh",
    "Roll No": 112,
    "City": "Morbi",
    "Branch": "MCA1A"
}

# Iterating over a list
print("Elements of the List:")
for item in numbers:
    print(item)

# Iterating over a string
print("\nCharacters of the String:")
for character in text:
    print(character)

# Iterating over a dictionary
print("\nElements of the Dictionary:")
for key, value in student.items():
    print(f"{key} -> {value}")
