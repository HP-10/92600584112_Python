num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

# Arithmetic Operations
print("\n======== Arithmetic Operations ========")
print("Sum:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Relational Operations
print("\n======== Relational Operations ========")
print(f"{num1} > {num2} =", num1 > num2)
print(f"{num1} < {num2} =", num1 < num2)
print(f"{num1} == {num2} =", num1 == num2)

# Logical Operations
print("\n======== Logical Operations ========")
print(f"{num1} > {num2} and {num1} > {num3} =",num1 > num2 and num1 > num3)

print(f"{num1} > {num2} or {num1} > {num3} =",num1 > num2 or num1 > num3)

print(f"Not ({num1} > {num2}) =",not (num1 > num2))
