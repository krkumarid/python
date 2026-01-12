def main():
    animals =("dog","cat","tiger","cat","wolf")    # Tuples can have duplicate values too

    number_animals = len( animals)
    print( number_animals )
   # Accessing the items in the Tuple
    print( animals[0])
    print( animals[4])

    print()
    for animal in animals:
        print(animal)

    print( "Looping with for")
    for i in range( 0, len( animals)):
        print( animals[i])
    print(" Looping with While")
    j =0
    while j <len(animals):
        print( animals[j])
        j = j+1


main()