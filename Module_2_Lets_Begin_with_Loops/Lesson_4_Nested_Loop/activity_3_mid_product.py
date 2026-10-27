
# Activity 3: Product of Middle Digit(s)

num = input("Enter a number: ")

digits = num.lstrip("-")
length = len(digits)

if length % 2 == 1:
    middle = int(digits[length // 2])
    product = middle
else:
    middle1 = int(digits[length // 2 - 1])
    middle2 = int(digits[length // 2])
    product = middle1 * middle2

print("Product of middle digit(s) =", product)
