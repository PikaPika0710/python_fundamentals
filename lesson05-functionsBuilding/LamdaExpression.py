from math import sqrt


def handle(f, x):
    return f(x)

def powerOfTwo(x):
    return x**2

def isEven(x):
    return x%2==0

def isOdd(x):
    return x%2!=0

def isPrime(x):
    for i in range(2, sqrt(x)+1):
        if x%i==0:
            return False
    return True


rs1 = handle(lambda x: x ** 2, 4)
print("rs1 = ", rs1)

rs1 = handle(powerOfTwo, 4)
print("rs1 = ", rs1)

rs2 = handle(lambda x: x % 2 == 0, 4)
print("rs2 = ", rs2)

rs2 = handle(isEven, 4)
print("rs2 = ", rs2)


