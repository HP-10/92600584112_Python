import random

print("=== Random Number Generation using random module ===")

print("Random integer:", random.randint(1, 100))
print("Random float:", random.random())
print("Random number between 1 and 10:", random.uniform(1, 10))
print("Random number from range:", random.randrange(1, 50))

numbers = [10, 20, 30, 40, 50]
random.shuffle(numbers)
print("Shuffled list:", numbers)

print("Random choice:", random.choice(numbers))
print("Random sample:", random.sample(numbers, 3))
