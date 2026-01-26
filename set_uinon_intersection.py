def main():

    numbers1 = { 1,2,3,4,5,6,7}
    numbers2 = {8,0,3,10,3,6,1}
    # Union
    print( numbers1.union(numbers2)) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 10}

    # Intersection

    print( numbers1.intersection( numbers2)) #{1, 3, 6}

    #Difference (-)

    print( numbers1.difference( numbers2)) #{2, 4, 5, 7}
    print("-")
    print( numbers1-numbers2) #{2, 4, 5, 7}

    print( numbers2.difference( numbers1)) #{0,8,10}

    # Symmetric_differecne

    print( numbers2.symmetric_difference( numbers1)) #{0, 2, 4, 5, 7, 8, 10}

    #Difference Update

    numbers1.difference_update( numbers2 )

    print( numbers1) #{2, 4, 5, 7}

    # issuperset()

    print( numbers1.issuperset( numbers2)) #False

    print( {1,2,3}.issuperset({1,2})) #True

main()