# Find the symmetric difference between two sets

set1 = {'blue', 'green'}
set2 = {'blue', 'yellow'}

print("Set 1:", set1)
print("Set 2:", set2)

result = set1.symmetric_difference(set2)

print("Symmetric difference:", result)

# Example B
set3 = {1, 2, 3, 4, 5}
set4 = {1, 5, 6, 7, 8, 9}

print("\nSet 3:", set3)
print("Set 4:", set4)

result2 = set3.symmetric_difference(set4)

print("Symmetric difference:", result2)