def main():


    animals = ["dog","donkey","duck"]

    # Insert at specific index using insert()

    animals.insert(1,"giraffe")

    print( animals) #['dog', 'giraffe', 'donkey', 'duck']
   
    more_animals = ["elephant","monkey"]

    # Extend the list using extend()
    animals.extend(more_animals)
    print( animals) #['dog', 'giraffe', 'donkey', 'duck', 'elephant', 'monkey']

    return
   


main()