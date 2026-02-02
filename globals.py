value =5

def do_somting():
    global value
    print(value)#5
    value =10
    print(value)#10
def main():
    do_somting()

    print( value) #10
main()