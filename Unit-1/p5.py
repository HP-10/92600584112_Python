l1 = []

user_name = input("Enter name of user: ")
l1.append(user_name)

user_age = int(input("Enter age of user: "))
l1.append(user_age)

user_city = input("Enter the city of user: ")
l1.append(user_city)

print("\n-- Full List --")
print(l1)


# Indexing
print("\n-- List Indexing --")
print("Name:", l1[0])
print("Age:", l1[1])
print("City:", l1[2])


# Slicing
print("\n-- Sliced List --")
print(l1[0:2])


# List Comprehension
print("\n-- List Comprehension --")

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [i * i for i in l2]

print("Original List:", l2)
print("Squares:", squares)
