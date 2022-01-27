def isPalindrome(string):
    for i in range(len(string)):
        if string[i] != string[len(string)-i-1]:
            return "{0} is not palindrome!".format(string)
    return "{0} is palindrome!".format(string)

def printS(string):
    for i in range(len(string)):
            print(string[i])


while(True):
    string = input("Input string: ")
    print(isPalindrome(string))
    print("Do you want to continue? Y/N", end=" ")
    if input() == "N":
        print("Thank You! Good Bye!")
        break



