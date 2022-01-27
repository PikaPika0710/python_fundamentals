def optimize(string):
    string = string.lower()
    s1= string
    s1 = s1.strip()
    arr = s1.split(' ')
    s2 = ""
    for i in arr:
        word = i
        if len(word.strip()) != 0:
            upperFirstCh = word[0].upper()
            for j in range(1, len(word)):
                upperFirstCh = upperFirstCh + word[j]
            s2 = s2 + upperFirstCh + " "

    return s2.strip()

def printS(string):
    s1 = string
    s1 = s1.strip()
    arr = s1.split(' ')
    s2 = ""
    for i in arr:
        print(i)


#string = input("Input the string: ")
string = "  TRần  côNG      viỆt"
print(string, len(string))
optimizedString = optimize(string)
print(optimizedString, len(optimizedString))