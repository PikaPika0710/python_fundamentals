mulList = [
    [1,2,3,4],
    [5,6,7,8],
    [2,3,4,5],
]
print(mulList)


for i in range(len(mulList)):
    for j in range (len(mulList[i])):
        print(mulList[i][j], end = " ")
    print()

print("*"*20)

for i in mulList:
    for j in i:
        print(j, end=" ")
    print()