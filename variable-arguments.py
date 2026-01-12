def describe_person( name, * attributes):
    print(name )
    print(type(attributes))
    for atr in attributes:
        print( atr )

def main():
    describe_person("rajeev","Sreesha","Kasi","Karthi","Asha")
    describe_person("Asha")
main()