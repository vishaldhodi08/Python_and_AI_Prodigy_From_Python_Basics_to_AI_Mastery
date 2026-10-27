
# Activity 1: Sum of Natural Numbers

# Input the number of terms
n = int(input("Enter the value of terms: "))

total = 0
i = 1

# Loop from 1 to n
while i <= n:
    total = total + i
    i = i + 1

print("\nSum =", total)
