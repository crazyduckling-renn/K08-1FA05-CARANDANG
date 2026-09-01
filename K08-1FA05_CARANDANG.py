import math

# Get the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Get the coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the differences between the coordinates
x_difference = x2 - x1
y_difference = y2 - y1

# Apply the distance formula using pow() and sqrt()
distance = math.sqrt(pow(x_difference, 2) + pow(y_difference, 2))

# Display the result
print(f"\nThe distance between the two points is: {distance:.2f}")

# Reflection:
# Using a library is more practical because it provides built-in functions
# that make calculations easier and reduce the amount of code we need to write.
# In this activity, sqrt() and pow() from the math library simplified the
# distance calculation instead of requiring us to create these functions ourselves.
