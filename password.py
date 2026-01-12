CORRECT_PWD="hello123"
correct = False
for i in range(0,3):
    password = input("Enter the password:")
    if( password == CORRECT_PWD):
        correct= True
        break
    else:
        print("Incorrect password")
if correct:
    print("Greetings Professor  Falcon")
else:
    print("Access denied")

