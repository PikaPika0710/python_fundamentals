
from random import randrange
def createArr(row,col):
    arr2D = []
    for i in range(row):
        arr1D = []
        for j in range(col):
            arr1D.append(randrange(-100, 100))
        arr2D.append(arr1D)
    return arr2D

def printArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end = " ")
        print()

def printRow(rowF, arr):
    for i in range(len(arr[rowF])):
        print(arr[rowF][i], end=" ")
    print()

def printCol(colF, arr):
    for i in range(len(arr)):
        print(arr[i][colF], end=" ")
    print()

def findMax(arr):
    max = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > max:
                max = arr[i][j]
    return max


row = int(input("Input row num: "))
col = int(input("Input col num: "))
arr2D = createArr(row, col)
printArr(arr2D)

rowF = int(input("Input row num to print: "))
printRow(rowF, arr2D)

colF = int(input("Input col num to print: "))
printCol(colF, arr2D)

print("Max of array is: ", findMax(arr2D))