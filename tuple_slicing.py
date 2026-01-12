def main():
    animals = ("goat","sheep","dog","elephant")
    print( animals[1]) #sheep
    print( animals[1:3]) #('sheep', 'dog')
    print( animals[0:3]) #('goat', 'sheep', 'dog')

    print()
    # We can use the negative index too. The negative index will start from the last, also  we can use negative index range to traverse back
    print( animals[-1]) #elephant
    print( animals[-3:-1]) #('sheep', 'dog')

    # We cannot do -ve to 0 range, we will get an empty tuple

    print( animals[-3:0]) #()

    extract = animals[0:2] # Slicing the tuple and assigning to another tuple
    print( type(extract)) #<class 'tuple'>
    print( extract) #('goat', 'sheep')

    #Extract the chars from a string using slicing
    name = "Sreesha"
    print( name[3]) #S
    print( name[1:4]) #reesha
    print( name[-4:-1]) #esh

    text ="It was the best of times"

    print( text[3]) #w
    print( text[0:2]) #It





main()