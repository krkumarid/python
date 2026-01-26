def main():
# Dictionaries are key value pair
    # | Key    |   Value    |
    # | apple  |   green    |
    fruits ={
        "apple":"green",        
        "orange":"orange",
        "banana":"yellow",

    }

    fruits1 = fruits.copy()

    fruits.pop("apple")

    print( fruits) #{'orange': 'orange', 'banana': 'yellow'}
    print()

    print( fruits1) #{'apple': 'green', 'orange': 'orange', 'banana': 'yellow'}

    fruits3 = { key:value  for (key,value) in fruits1.items() }
    print("===With Comprehension =====================")
    print( fruits3)


main()