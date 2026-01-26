def main():
# Dictionaries are key value pair
    # | Key    |   Value    |
    # | apple  |   green    |
    fruits ={
        "apple":"green",        
        "orange":"orange",
        "banana":"yellow",

    }
    # Using del
    del fruits["apple"]
    print( fruits) #{'orange': 'orange', 'banana': 'yellow'} 

    # Deleting items using pop() method
    color = fruits.pop("banana")
    print( color )
    print( fruits ) #{'orange': 'orange'}

main()