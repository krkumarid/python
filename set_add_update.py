

def main():
    numbers = {1,2,3}

    print( numbers ) #{1, 2, 3}
# Adding  items to the set
    numbers.add( 5)
    numbers.add(7)

    print( numbers ) #{1, 2, 3, 5, 7}

    # Update the set with another set

    numbers2 = {10,20,30}

    numbers2.update( numbers )
    print( numbers2 ) #{1, 2, 3, 5, 7, 10, 20, 30}

    numbers2.update( ["cat","dog"]) #{1, 2, 3, 5, 7, 10, 20, 'cat', 'dog', 30}

    print( numbers2)

main()