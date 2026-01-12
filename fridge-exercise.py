# The Fridge
"""

Get the user enter a temperature in celsius

<0 :Print  "Fride too cold"
0 - 4 : Print "Fridge OK"
4  - 6 : Print "Fridge too warm"
> 6 : Print :"Fridge broken"

"""

temp_C = input("Enter the fridge temperature in C : ")
temp_int = int(temp_C)
if( temp_int ) < 0 :
    print("Fridge is too cold")
elif ( temp_int >=0 and temp_int <=4 ):
    print("Fridge OK")
elif(  temp_int>=4 and temp_int<=6):
    print("Fridge too warm")
elif( temp_int >6 ):
    print("Fridge is broken")
else:
    print("This temperatue is not valid")
print ("The program ends")
