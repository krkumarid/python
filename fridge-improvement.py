# The Fridge
"""

Get the user enter a temperature in celsius

<0 :Print  "Fride too cold"
0 - 4 : Print "Fridge OK"
4  - 6 : Print "Fridge too warm"
> 6 : Print :"Fridge broken"

"""

temperature  = input("Enter the fridge temperature in C : ")
temperature = float(temperature)

STATUS_DEFAULT = "Fridge is broken"
STATUS_OK = "Fridge OK"
STATUS_WARM = "Fridge too warm"
STATUS_COLD = "Fridge is too cold"
status = STATUS_DEFAULT

if( temperature ) < 0 :
    status = STATUS_COLD
elif ( temperature >=0 and temperature <=4 ):
    status = STATUS_OK
elif(  temperature>=4 and temperature<=6):
    status = STATUS_WARM
elif( temperature >6 ): 
    status = STATUS_DEFAULT
    
print(status)
print ("The program ends")
