"""
Docstring for password-exercise

Write a  program that asks the user to enter a a password and compares it to a hard -coded password.

If the password is correcr, the program prints "Greetings Professsor Falcon" exists

If the password is incorrect, the program prints "Access denied" and then asks for the password again

The program will ask for the password three times if necessary
After that , it exists
"""

PASSWORD = "asha"
for i in range(3):
    password = input("Enter the password: ")
    if password == PASSWORD:
        print("Greetings Professsor Falcon")
        break
    else:
        print("Access denied")
        continue   
print(" Program exits")