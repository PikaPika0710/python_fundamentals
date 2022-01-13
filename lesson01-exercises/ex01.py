#input r and find the area and perimeter of the circle(r)
import math
try:
    r = float(input("Input the radius: "))
    print("Perimeter: ", 2*math.pi*r)
    print("Area: ", math.pi*r**2)
except:
    print("Error!")