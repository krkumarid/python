numbers = { 1,2,3,1}

print( numbers) # {1, 2, 3}
# All the items in a set are unique.

# finding the u unique items in a list

numbers_list = [2,3,3,2,5,6]

print( set( numbers_list)) #{2, 3, 5, 6}

for number in numbers:
    print( number )

print( 3 in numbers) #True

print( 5 in numbers) # False

""""
list : odered  "in" is slow,mutable -- can change
Tuple : Ordered "in" is slow , immutable - cannot change
Set : is not ordered. "in" is fast- mutable --can change

"""