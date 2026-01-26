def main():
# Dictionaries are key value pair
    # | Key    |   Value    |
    # | apple  |   green    |
    fruits ={
        "apple":"green",        
        "orange":"orange",
        "banana":"yellow",

    }


    keys = fruits.keys() #dict_keys(['apple', 'orange', 'banana'])
    values = fruits.values() #ict_values(['green', 'orange', 'yellow'])
    items = fruits.items() #dict_items([('apple', 'green'), ('orange', 'orange'), ('banana', 'yellow')])

    print( keys)
    print( values)
    print( items)

    keys_list = list(keys)
    print( keys_list) #['apple', 'orange', 'banana']


    fruits["raspberry"] = "red"

    print( keys ) #dict_keys(['apple', 'orange', 'banana', 'raspberry'])

    print()

    print( keys_list ) #['apple', 'orange', 'banana']



main()
