
# Activity 1: Character Occurrence

word = input("Enter a word: ")
character = input("Enter the character to search: ")

count = 0

for letter in word:
    if letter == character:
        count += 1

print("Character occurs", count, "times")
