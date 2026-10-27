character = input("Enter a character: ")

if len(character) == 1 and character.isalpha():
    print("The character is an alphabet.")
else:
    print("The character is not an alphabet.")