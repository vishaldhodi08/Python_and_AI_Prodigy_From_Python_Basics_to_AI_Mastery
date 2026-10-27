try:
    age_input = input("Enter your age: ")
    age = int(age_input)

    if age < 0:
        print("Error: Age cannot be negative.")
    else:
        print("Your age is:", age)

        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")

except ValueError:
    print("Error: Please enter a valid whole number for your age.")