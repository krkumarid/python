def accept_argumnets( number,*args,**kwargs):
    print( number )
    print()
    for arg in args:
        print( arg )
    print()
    for kwarg in kwargs:
        print( kwarg,": ", kwargs[ kwarg])

def main():

    accept_argumnets( 1)
    accept_argumnets( number =2 )
    accept_argumnets(2,"Rajeev","Sreesha","Kasi","Karthi")
    accept_argumnets(3,"Rajeev","Sreesha","Kasi","Karthi",Name="Rajeev",Age=46, color="black")

main()