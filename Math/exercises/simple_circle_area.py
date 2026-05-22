# Ask for radius and compute area = 3.14 * r * r
import math

radius = float(input("Please enter the radius of the circle: "))
area = radius * radius * math.pi
#or use : area = radius * radius * 3.14
print(f"The area of the circle is {area:0.2f}")