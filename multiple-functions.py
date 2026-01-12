PASSWORD = "asha"

def greeting():
    print("Welcome ")

def check_password():
    password = input("Enter your password >")

    if password == PASSWORD:
        print("Access granted.")
    else:
        print("Access denied.")

def main():
    print("Starting....main()")
    greeting()
    check_password()
    
main()