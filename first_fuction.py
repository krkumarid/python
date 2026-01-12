"""
Docstring for first_fuction


"""
#Defining the function
def ask_user_status():
    response = input("How are you? : ")
    if response =="OK" or response == "ok":
        print("Excellent")
    else:
        print("Oh no.")
# Calling the function
ask_user_status()