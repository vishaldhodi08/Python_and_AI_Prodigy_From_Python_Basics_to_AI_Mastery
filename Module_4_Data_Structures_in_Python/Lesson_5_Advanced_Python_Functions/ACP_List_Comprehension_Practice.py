# 1. Create a list of odd numbers under the user's input value

number = int(input("Enter a number: "))

odd_numbers = [n for n in range(number) if n % 2 != 0]

print("Odd numbers:", odd_numbers)


# 2. Capitalize the first letter of every fruit

fruits = ["apple", "banana", "mango", "orange", "grapes"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits:", fruits)
print("Capitalized fruits:", capitalized_fruits)