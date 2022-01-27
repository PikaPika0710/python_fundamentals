def sum(n,m=4, k=1):
    sum = 0
    for i in range(1, m+n+k, 1):
        sum += i
    return sum

a = sum(5)
print(a)
b = sum(5,1)
print(b)
c = sum(5, k=2)
print(c)

for item in ["abc", "xyz", "567"]:
    print(item) #default of the second parameter is "\n"

for item in ["abc", "xyz", "567"]:
    print(item, end="\t")  #change the default to "\t"