def main():
# Dictionaries are key value pair
    # | Key    |   Value    |
    # | apple  |   green    |
    fruits ={
        "apple":"green",        
        "orange":"orange",
        "banana":"yellow",

    }
    color = fruits.get("mango")
    print( color)

    print( type(color))

    # We can assign defalult value for non existing item
    color1  = fruits.get("mango","red") #red

    print( color1)

main()