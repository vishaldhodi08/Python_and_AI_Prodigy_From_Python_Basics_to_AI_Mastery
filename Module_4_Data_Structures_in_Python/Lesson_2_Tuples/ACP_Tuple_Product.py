# Calculate the product of numbers entered by the user

numbers = tuple(
    map(int, input("Enter numbers separated by spaces: ").split())
)

product = 1

for number in numbers:
    product *= number

print("Tuple:", numbers)
print("Product of all numbers:", product)