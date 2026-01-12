"""
Docstring for boolean-operator-exersice
Ask the user
1. Are you a student
2. Do you have pets?
3. Do you smoke?

The progrm automatically decides whether a poperty you have applied to rent is available to you.

It should print a appropriate response, like "Property available" or Property unavailable".

The program applies these criteria

If you are student , you can only rent the property if you don't have pets and don't smoke
If you are not a student, you can rent the property  if you smoke or have pets, but not is you both smoke and also have pets

"""

student = input( "Are you a student?(y/n) : ")
pets = input("Do you have pets? (y/n) :")
smoke = input("Do you smoke? (y/n) :")
can_rent = False

IS_STUDENT = student =="y"
HAS_PETS = pets=="y"
DOES_SMOKE = smoke == "y"

if IS_STUDENT:
    if HAS_PETS and DOES_SMOKE:
        can_rent == False
    else:
        can_rent =True
else:
    if DOES_SMOKE and HAS_PETS:
        can_rent =False
    else:
        can_rent =True
if can_rent:
    print("The property is available")
else:
    print("The property is not available")