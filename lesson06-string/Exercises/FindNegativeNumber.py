def negativeNumberInStrings(str):
    negativeNumbers = []
    arr = str.split('-')
    for i in arr:
        word = i
        if len(word.strip()) != 0:
            if word[0].isnumeric():
                s="-"+word[0];
                for j in range(1, len(word)):
                    if word[j].isnumeric():
                        s=s+word[j];
                    else:
                        break
                negativeNumbers.append(s)

    return negativeNumbers
def printS(str):
    negativeNumbers = []
    arr = str.split('-')
    for i in arr:
        print(i)

str = "-10abc-5xyz-12k9l-45-p"
printS(str)
arr = negativeNumberInStrings(str)
print(arr)