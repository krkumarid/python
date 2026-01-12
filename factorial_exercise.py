
def calculate_fact( num ):
    fact =1
    for i in range( 2, num+1 ):
        fact = fact * i
    return fact

def factorial( num ):
    if ( num == 0 or num ==1 ):
        return 1
    else:
        result =1
        while( num>=1):
            result = result*num
            num = num-1
    return result
# recuurssive
def recurssive( num ):
    if ( num == 0 or num ==1 ):
        return 1
    else:
        return num * recurssive( num-1)

def main():

    #print( calculate_fact(5))
    #print( factorial(10))
    print( recurssive(7))


main()