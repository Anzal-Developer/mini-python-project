def addressval(address):
    Dot =address.find('.')
    at = address.find('@')
    if (Dot == -1):
        print("invalid address: missing")
    elif (at == -1):
        print("invalid address: missing @")
    else:
        print("valid address")


print("This program will decide if your input is a valid email address or not")
while (True):
    print("An email address must contain an '@' sign and a '.' sign")
    x = input("Please enter an email address to validate or type 'exit' to quit: ")


    addressval(x)
            