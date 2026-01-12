def main():
    elements = ( True,3.2,7,"goat") # A Tuple can contain all types of data

    #Unpacking
    ( is_raining,weight,volume,animal) = elements

    print( is_raining)
    print( weight)
    print( volume)
    print( animal)


    fruits = ("apple","orange","banana","strawberry","pear")

    ( fruit1,fruit2, fruit3,*more_fruits) = fruits

    print()
    print( fruit1) #apple
    print( fruit2) #orange
    print( fruit3) #banana
    print( more_fruits) # prints a tuple
    # We cannot have a tuple with a single item

    one_item =("goat") 

    print( type( one_item)) # <class 'str'>

    

main()