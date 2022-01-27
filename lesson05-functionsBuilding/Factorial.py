def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print("{0}! = {1}".format(6, factorial(6)))