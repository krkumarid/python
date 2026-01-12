def greet( name ):
    print( "Hello " + name )

def create_greeting( name ):
    return "Hi " + name

def main():
    name  ="Asha"
    
    greet( name )
    greeting = create_greeting(name)
    print( greeting )



main()