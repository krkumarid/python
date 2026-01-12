def get_user_info():

    name = input("Enter your  name >")
    age = input("Enter your age >")
    return name,age

def main():
    
    name, age = get_user_info()
    print( name + " :" + age )



main()