""""
Print all the cubic numbers up to and including 729

Print all the square numbers upto and includinf 729

Which cubic numbers are also square number?

Which cubic numbers are not square numbers?




"""


def main():

    cubic_set = { x**3 for x in range(10)} # x**3 -> X to the power of 3
    print( cubic_set)

    square_set = { x**2 for x in range(28)} #x**2 -> x to the power of 2
    print( square_set)

    print( cubic_set.intersection( square_set)) #{0, 1, 64, 729}

    print( cubic_set.difference( square_set)) #{512, 8, 343, 216, 27, 125}

main()