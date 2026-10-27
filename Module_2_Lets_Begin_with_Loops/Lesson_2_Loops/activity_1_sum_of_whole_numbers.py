
# Activity 1: Sum of Whole Numbers

# Input an integer value
n = int(input("Enter the number whose sum you want to find: "))

total = 0

# Iterate from 1 to n
for i in range(1, n + 1):
    total = total + i

print("\nSum =", total)
