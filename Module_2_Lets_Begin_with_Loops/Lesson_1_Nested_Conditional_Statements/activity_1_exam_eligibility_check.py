
# Activity 1: Exam Eligibility Check

# Ask whether the student has a medical cause
medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()

if medical_cause == "Y":
    print("You are allowed to take the exam.")
elif medical_cause == "N":
    attendance = float(input("Enter your attendance percentage: "))

    if attendance >= 75:
        print("You are allowed to take the exam.")
    else:
        print("You are not allowed to take the exam.")
else:
    print("Invalid input. Please enter Y or N.")
