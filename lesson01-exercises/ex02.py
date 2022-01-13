#input the total second and find the axact time (hh:MM:ss)
try:
    total = int(input("Input the total second: "))
    hour = (total//3600)%24;
    minute = (total%3600)//60
    second = (total%3600)%60;
    print("Time: {0}:{1}:{2}".format(hour, minute, second))
except:
    print("Error!")