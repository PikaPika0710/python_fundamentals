from random import randrange

while True:
    count = 0
    while True:
        count = count + 1
        if count > 7:
            print("GAME OVER")
            break
        print("Guessing times: ", count)
        machineNumber = randrange(1, 101)
        #print(machineNumber)
        guessNumber = int(input("Enter a number: "))
        if guessNumber == machineNumber:
            print("***CORRECT! The number is {0}***.".format(machineNumber))
            print("YOU WIN!")
            break
        if guessNumber < machineNumber:
            print("The number you guess is smaller than machine number")
        elif guessNumber > machineNumber:
            print("The number you guess is bigger than machine number")
    print("Do you want to continue: (Y/N)")
    if input() == "N":
        print("GOODBYE...")
        exit()




