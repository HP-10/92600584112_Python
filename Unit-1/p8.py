# ================= MUTABLE OBJECT =================
print("========== MUTABLE OBJECT ==========")

lst = ["Harsh", "Morbi"]

print("Original List:", lst)

# List can be modified
lst.append("MCA1A")

print("After append:", lst)

# Modifying an existing element
lst[0] = "Raj"
print("After modification:", lst)


# ================= IMMUTABLE OBJECT =================
print("\n========== IMMUTABLE OBJECT ==========")

tple = (1, 2, 3, 4, 5)

print("Original Tuple:", tple)

# Creating a new tuple
new_tple = tple + (6, 7)
print("New Tuple:", new_tple)

print("\nTuple cannot be modified directly because it is immutable.")
