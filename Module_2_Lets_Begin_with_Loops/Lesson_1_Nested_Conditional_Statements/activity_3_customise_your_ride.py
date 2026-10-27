
# Activity 3: Customise Your Ride

print("Select your ride:")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\nWhat type of bike?")
    print("1. Scooty")
    print("2. Scooter")

    choice2 = int(input("Enter your choice: "))

    if choice2 == 1:
        print("You have selected Scooty.")
    elif choice2 == 2:
        print("You have selected Scooter.")
    else:
        print("Invalid bike choice.")

elif choice == 2:
    print("\nWhat type of car?")
    print("1. Sedan")
    print("2. SUV")

    choice3 = int(input("Enter your choice: "))

    if choice3 == 1:
        print("You have selected Sedan.")
    elif choice3 == 2:
        print("You have selected SUV.")
    else:
        print("Invalid car choice.")

else:
    print("Wrong choice!")
