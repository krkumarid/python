"""
Write a program that asks the user to enter a name

if the user enters a name in the list below , respond with the age of  the person entered. Otherwise print "Unknown person"

Make the program keep asking foe names like this until the user enters "quit" .then the program exits

Star by puttign the names and ages in a dictionary



"""
def create_lookup( people, ages ):

    lookup = dict()
    for name, age in zip(people,ages):
        lookup[name.casefold()] = age

    return lookup

def user_loop( lookup ):

    
    while(True):
        user_input = input("Enter a name, or 'quit' >>  ")
        
        if user_input == "quit":
            break
        age = lookup.get( user_input.casefold() )
        print( age)
        if age is None:
            continue

        print( user_input + " is "+ str(age) + "  years old")


def main():

    people = ["Asha", "Rajeev","Sreesha","Kasi","Karthi","Paru","Smitha","Rajani"]
    age =[47,46,44,15,7,19,45,52]

    lookup = create_lookup( people=people, ages=age)
    user_loop( lookup= lookup)
    return 

main()