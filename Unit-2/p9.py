# Creating an iterable
fruits = ["Apple", "Banana", "Cherry"]

print("Iterable:", fruits)

# Creating an iterator from the iterable
fruit_iterator = iter(fruits)

print("\nElements obtained using iterator:")

# Accessing elements one by one
print(next(fruit_iterator))
print(next(fruit_iterator))
print(next(fruit_iterator))