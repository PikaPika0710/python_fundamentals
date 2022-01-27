def sumGCD(n):
    sum = 0
    for i in range(1, n//2+1):
        if n%i==0:
            sum=sum+i

    return sum

def isPerfectNumber(n):
    if(sumGCD(n) == n):
        return "{0} is perfect number".format(n)
    else:
        return "{0} is not perfect number".format(n)

def isAbundantNumber(n):
    if (sumGCD(n) > n):
        return "{0} is abundant number".format(n)
    else:
        return "{0} is not abundant number".format(n)

N = int(input("Input n: "))
print(isPerfectNumber(N))
print(isAbundantNumber(N))

