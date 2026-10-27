
# Activity 2: Reverse a String

string = input("Please enter your own string: ")

string2 = ""

# Loop through the string
for i in string:
    string2 = i + string2

print("\nThe Original String =", string)
print("The Reversed String =", string2)
