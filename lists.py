def main():
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    #Slicing the list
    print(fruits)
    print(fruits[1:4])  # ['banana', 'cherry', 'date']

    #Count the number of elements in the list
    print(len(fruits))  # 5


    # Empty list or tuple

    test1 = tuple() #Emoty tuple
    test2 = list() # Empty list

    print(type(test1)) #<class 'tuple'>
    print(type(test2)) #<class 'list'>

    test3 = () # Empty tuple
    test4 = [] # Empty list
    print(type(test3)) #<class 'tuple'>
    print(type(test4)) #<class 'list'>

    #Converting tuple to list
    animals = ("lion", "tiger", "bear")
    animal_list = list(animals)

    print(type(animal_list)) #<class 'list'>'

    print( animal_list ) #['lion', 'tiger', 'bear']

    for item in animal_list:
        print( item )

    for i in range( len(animal_list)):
        print( f'Index {i} has value {animal_list[i]}')
main()