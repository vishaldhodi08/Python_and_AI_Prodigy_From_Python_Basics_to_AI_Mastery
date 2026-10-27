
# Activity 3: Armstrong Number

# Take input from the user
num = int(input("Enter a number: "))

# Initialize sum
total = 0
temp = num

# Find the sum of cubes of each digit
while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

# Display the result
if num == total:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
