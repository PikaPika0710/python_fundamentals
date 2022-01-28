from random import randrange

arr2D = []
row = 3
col = 3
for i in range(row):
    arr1D = []
    for j in range(col):
        arr1D.append(randrange(-100,100))

    arr2D.append(arr1D)

print(arr2D)