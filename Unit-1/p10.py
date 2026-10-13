n = int(input("Enter a number: "))

# Factorial
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

print("Factorial is:", factorial(n))

# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")
