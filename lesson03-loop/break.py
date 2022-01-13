while True:
    number = int(input("Enter a number: "))
    print("Entered number: ", number)
    string = input("Do u want to continue? (Y/N): ")
    if string == "N":
        break
print("After while loop!")