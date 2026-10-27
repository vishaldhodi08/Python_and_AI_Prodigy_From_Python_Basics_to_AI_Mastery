import random
import string

# Ask the user for the desired password length
length = int(input("Enter password length (minimum 3): "))

if length < 3:
    print("Password length must be at least 3.")
else:
    # Include lowercase, uppercase, and numeric characters
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Ensure the password contains at least one of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]

    # Fill the remaining positions randomly
    password += random.choices(characters, k=length - 3)

    # Shuffle the password characters
    random.shuffle(password)

    # Convert the list into a string
    password = "".join(password)

    print("Generated password:", password)