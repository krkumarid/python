def greet( username, age  ):
    print("Hello  " +  username +" You are  "+ age +" years old")

def main():
    name = input("What is your name? > ")
    age = input("What  is your age? >")
    greet(name,age )

main()