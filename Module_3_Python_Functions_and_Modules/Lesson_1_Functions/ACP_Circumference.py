import math

def circumference(radius):
    return 2 * math.pi * radius

radius = float(input("Enter the radius of the circle: "))

if radius >= 0:
    result = circumference(radius)
    print(f"Circumference of the circle: {result:.2f}")
else:
    print("Radius cannot be negative.")