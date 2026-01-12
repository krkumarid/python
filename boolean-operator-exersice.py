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
STUDNET = False
PETS =False
SMOKE= False
student = input( "Are you a student?(y/n) : ")
pets = input("Do you have pets? (y/n) :")
smoke = input("Do you smoke? (y/n) :")


IS_STUDENT = student =="y"
HAS_PETS = pets=="y"
DOES_SMOKE = smoke == "y"

student_can_rent = IS_STUDENT and not HAS_PETS and not DOES_SMOKE
non_student_can_rent = not IS_STUDENT and not( HAS_PETS and DOES_SMOKE)

can_rent = student_can_rent or non_student_can_rent

print("Can rent :" + str( can_rent))

