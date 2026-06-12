x = input("Password: ")
if (x == "123"):
    print("Access Granted!")
    name = input("What is your name? ")
    print("Welcome to Wavelab, " + name + "!")

while (x != "123"):
    x = input("Access Denied!\nTry Again ")
    if (x == "123"):
        print("Access Granted!")
        name = input("What is your name? ")
        print("Welcome to Wavelab, " + name + "!")
