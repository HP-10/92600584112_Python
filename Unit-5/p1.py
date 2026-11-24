# 1. Syntax Error
# print("Hello"   # Missing closing bracket

# 2. Name Error
try:
    print(x)
except NameError:
    print("Name Error occurred")

# 3. Type Error
try:
    print(10 + "Hello")
except TypeError:
    print("Type Error occurred")

# 4. Value Error
try:
    num = int("abc")
except ValueError:
    print("Value Error occurred")

# 5. Zero Division Error
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Zero Division Error occurred")

# 6. Index Error
try:
    a = [10, 20, 30]
    print(a[5])
except IndexError:
    print("Index Error occurred")

print("Program completed")