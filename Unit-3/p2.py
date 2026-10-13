print("=== Import Module in different types ===")

import calculator
print("Import using Simple method:")
print(calculator.add(5, 10))
print(calculator.sub(5, 10))

import calculator as calc
print("Import using Alias:")
print(calc.mul(5, 10))
print(calc.div(5, 10))

from calculator import add, sub
print("Import using specific Functions:")
print(add(20, 10))
print(sub(20, 10))

from calculator import mul as multiply, div as divide
print("Import using Specific Functions with Alias:")
print(multiply(4, 5))
print(divide(20, 4))

from calculator import *
print("Import All Functions:")
print(add(3, 3))