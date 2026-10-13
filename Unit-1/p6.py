#================= TUPLE =================

tupl1 = ('Harsh', 21, 'Morbi', 21, 21)

print("========== TUPLE ==========")

print("Full Tuple:", tupl1)

# Tuple indexing
print("First Element:", tupl1[0])
print("Third Element:", tupl1[2])

# Tuple slicing
print("Tuple Slicing:", tupl1[0:3])

# Tuple count
print("Count of 21:", tupl1.count(21))

# Tuple index
print("Index of Morbi:", tupl1.index('Morbi'))


# ================= SET =================

print("\n========== SET ==========")

set1 = {'Harsh', 21, 'Morbi'}

# Display original set
print("Original Set:", set1)

# Add an element
user_education = input("Enter education details: ")
set1.add(user_education)
print("After Adding Element:", set1)

# Add multiple elements
set1.update({'Python', 'Computer Science'})
print("After Updating Set:", set1)

# Remove an element
# set1.discard(21)
set1.remove(21)
print("After Removing 21:", set1)

# Check membership
print("Is 'Harsh' present?", 'Harsh' in set1)

# Display number of elements
print("Set Length:", len(set1))
