n = int(input("Enter a number: "))
s =0
if n%2==0:
    for x in range(2,n+1, 2):
        s+=x
else:
    for x in range(1,n+1, 2):
        s+=x
print("s = ", s)