import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x_difference = x2 - x1
y_difference = y2 - y1

distance = math.sqrt(pow(x_difference, 2) + pow(y_difference, 2))

print(f"\nThe distance between the two points is: {distance:.2f}")
