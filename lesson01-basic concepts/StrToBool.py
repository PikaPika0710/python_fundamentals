

def StrToBool(s):
    return s.lower() in ("yes", "true", "t", "1")

s =StrToBool(input("Input a boolean: "))
print("You entered: ", s)
print("Data type: ", type(s))