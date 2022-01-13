month = int(input("Input any month to see amount of day: "))
if month in (1,3,5,7,8,10,12) :
    print(month, " has 31 days!")
elif month in (4,6,9,11):
    print(month, " has 30 days!")
elif month==2:
    year = int(input("Input a year: "))
    if ((year %4==0 and year%100!=0 ) or (year%400==0)):
        print(month, " has 29 days!")
    else:
        print(month, " has 28 days!")
else:
    print(month, " is not valid!")