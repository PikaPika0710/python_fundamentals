from builtins import print

from numpy import finfo


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def printFibonacci(n):
    for i in range(1,n+1):
        print(fibonacci(i), end=" ")


N = int(input("Input n: "))

print("The Fibonacci number at {0} is {1}".format(N, fibonacci(N)))
printFibonacci(N)