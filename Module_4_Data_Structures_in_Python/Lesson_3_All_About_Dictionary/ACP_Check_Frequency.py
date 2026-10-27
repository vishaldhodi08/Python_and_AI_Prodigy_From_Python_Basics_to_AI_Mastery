# Check the frequency of a value in a dictionary

test_dictionary = {
    "Codingal": 3,
    "is": 2,
    "best": 2,
    "for": 2,
    "Coding": 1
}

print("Test Dictionary:")
print(test_dictionary)

value = input("Enter the value you want to check: ")

frequency = test_dictionary.get(value, 0)

print("Frequency of", value, ":", frequency)