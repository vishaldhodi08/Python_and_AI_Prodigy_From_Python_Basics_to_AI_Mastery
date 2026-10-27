import math

# Take angle input from the user in degrees
angle = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
radians = math.radians(angle)

# Calculate trigonometric values
sin_value = math.sin(radians)
cos_value = math.cos(radians)

print("Angle:", angle, "degrees")
print("Sine value:", round(sin_value, 4))
print("Cosine value:", round(cos_value, 4))

# Check whether tangent is defined
if abs(cos_value) < 1e-10:
    print("Tangent value is undefined.")
else:
    tan_value = math.tan(radians)
    print("Tangent value:", round(tan_value, 4))