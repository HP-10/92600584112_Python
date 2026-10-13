num = int(input("Enter the table number: "))

print("\nMultiplication Table of", num)
print("-" * 30)

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")