
# ACP: Power Calculator

base = float(input("Enter the base number: "))
n = int(input("Enter the power: "))

result = 1

if n < 0:
    print("Please enter a non-negative power.")
else:
    for i in range(n):
        result = result * base

    print(f"{base} raised to the power {n} is {result}")
