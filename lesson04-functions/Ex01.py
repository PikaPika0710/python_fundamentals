from math import sqrt

n = int(input("Input n: "))
sum = 0
for i in range(n):
    sum = sum+2
    sum = sqrt(sum)
print("S({0}) = {1}".format(n, sum))

