def main():
    try:
        while True:
            greeting = input("Password: ")
            if greeting == "123":
                name = input("Hello! What is your name? ")
                print("Welcome to Wavelab, " + name + "!")
                break
            else:
                print("Wrong password, try again.")
    except KeyboardInterrupt:
        print("\nGoodbye.")


if __name__ == "__main__":
    main()