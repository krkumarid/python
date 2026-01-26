def main():

    numbers = [[1,2,3], [4,5,6],[7,8]]
    sublist = numbers[1]
    print( sublist) # [4, 5, 6]

    print( sublist[2]) #6

    print( numbers[2][1]) #8

    for x in numbers:
        for y in x:
            print(y, end="\t")
        print()

    # Using range
    print( "Using range")
    for i in range(0, len( numbers)):
        for j in range( 0,len(numbers[i])):
            print( numbers[i][j],end="\t")
        print()
main()