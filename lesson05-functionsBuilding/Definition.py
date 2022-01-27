def PTB1(a, b):
    if(a==0 and b==0):
        return "PT vo so nghiem"
    elif (a==0 and b!=0):
        return "PT vo nghiem"
    else:
        return "x = {0}".format(round(-b/a,2))

def printData(data):
    print(data)

kq = PTB1(5,8)
print(kq)
kq1= PTB1(0,0)
print(kq1)
kq2 = PTB1(0,5)
print(kq2)

printData("Ket qua la: {0}".format(kq))

p = printData("HelloWorld")
print(p)