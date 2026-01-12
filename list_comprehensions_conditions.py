def main():

    number1  = [x for x in range(0, 10)]
    print( number1 ) #[0,1, 2, 3, 4, 5, 6, 7, 8, 9]

    number2  = [x for x in range(0, 10) if x > 5 ] 
    print( number2 ) #[6, 7, 8, 9]

    print()
    numbers3  = [x for x in range(0, 10) if x % 2 == 0 ]
    print( numbers3 ) #[0, 2, 4, 6, 8]

    print()
    

    return
main()