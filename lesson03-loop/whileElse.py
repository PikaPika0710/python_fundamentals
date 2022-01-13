count = sum = 0
while count < 5:
    n = int(input("Enter a number for calculating the average: "))
    if n<0:
        print(n, "is not valid!")
        break
    sum+=n;
    count=count+1;
#final
else:
    print("Average: ", sum/count)
