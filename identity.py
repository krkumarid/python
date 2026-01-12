
def greet( name ):
    print( id(name))
    name="RAjeev"
    print( id(name))
    print("Hello " + name )


def main():
    name  ="Asha"
    print( id(name))
    greet( name )


main()