from math import sqrt
print("TRIANGLE PROGRAM!")
print("Input the 3 valid sides of triangle!")
a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))
perimeter = a + b + c
p = perimeter/2
area = sqrt(p*(p-a)*(p-b)*(p-c))
print("Perimeter of triangle({0},{1},{2}) is: {3} ".format(a,b,c,perimeter))
print("Area of triangle({0},{1},{2}) is: {3} ".format(a,b,c,round(area,3)))
