numbers = [10, 20, 30, 40]

# List Comprehension
squares = [num ** 2 for num in numbers]

# Dictionary Comprehension
cubes = {num: num ** 3 for num in numbers}

# Set Comprehension
remainders = {num % 3 for num in numbers}
"""
10/3 Rminder -> 1,
20/3 Rminder -> 2,
30/3 Rminder -> 0,
40/3 Rminder -> 1,
Ans={0,1,2} - Because It sort value & do not repeats values.
"""

# Display the results
print("Original List:", numbers)
print("List Comprehension - Squares:", squares)
print("Dictionary Comprehension - Cubes:", cubes)
print("Set Comprehension - Remainders:", remainders)
