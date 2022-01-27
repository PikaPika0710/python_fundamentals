def gcd(a,b):
    """This function is used for find the greatest common divisor!!!"""
    if a==b:
        return a
    else:
        while a!=b :
            if a<b:
                b = b-a
            elif a>b:
                a = a-b

    return a

print(gcd(9,6))