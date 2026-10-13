# Different Data Types
name = "Harsh"          # String
age = 21                # Integer
height = 5.8            # Float
student = True          # Boolean

print("========== DATA TYPES ==========")

print("Name:", name)
print("Type:", type(name))

print("Age:", age)
print("Type:", type(age))

print("Height:", height)
print("Type:", type(height))

print("Student:", student)
print("Type:", type(student))


# Type Casting
print("\n========== TYPE CASTING ==========")

num = "25"

print("Original value:", num)
print("Original type:", type(num))

num = int(num)
print("After int casting:", num)
print("Type:", type(num))

num = float(num)
print("After float casting:", num)
print("Type:", type(num))

num = str(num)
print("After string casting:", num)
print("Type:", type(num))
