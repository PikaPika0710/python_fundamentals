from random import randrange

arr = []
n = int(input("Input N: "))
for i in range(n):
    arr.append(randrange(-100,100))

print(arr)

e1 = int(input("Input one element to add: "))
arr.append(e1)
print(arr)

e2 = int(input("Input one element to delete: "))
while arr.count(e2) > 0:
    arr.remove(e2)
print(arr)


