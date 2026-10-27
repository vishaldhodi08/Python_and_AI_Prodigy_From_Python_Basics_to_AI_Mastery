# Input a word
text = str(input("Enter a string: "))

# Reverse the string using a step value of -1
revText = text[::-1]
text = revText

print("Reverse of Given String is:")
print(text)