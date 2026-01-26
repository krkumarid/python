def main():
# Dictionaries are key value pair
    # | Key    |   Value    |
    # | apple  |   green    |
    fruits ={
        "apple":"green",        
        "orange":"orange",
        "banana":"yellow",

    }
    # Looping through dictionaries
    for fruit in fruits:
        print(fruit +":"+ fruits[fruit])

    # Using the keys
    print("Using the keys")
    for key in fruits.keys():
         print( key + ":"+ fruits[key])
    print( "apple" in fruits) # True, Checking the presece of apple in the dictionary.

    for fruit in fruits.items():
        print( fruit )  #('apple', 'green')
                        #('orange', 'orange')
                        #('banana', 'yellow') 

    # Unpacking the dictionary to a tuple
    for( fruit, color) in fruits.items():
            print( fruit +","+ color )

    # Using the valuee

    for value in fruits.values():
         print( value)

main()