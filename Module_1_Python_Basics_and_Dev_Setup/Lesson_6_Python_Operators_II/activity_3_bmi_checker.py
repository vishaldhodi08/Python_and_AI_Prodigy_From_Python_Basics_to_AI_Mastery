height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

if height <= 0 or weight <= 0:
    print("Please enter valid height and weight.")
else:
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    print("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You are in the healthy weight range.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are in the obesity range.")