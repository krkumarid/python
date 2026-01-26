numbers = { x for x in range(15)}

print( numbers ) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

# Removing the item from the set

numbers.remove( 6 ) #{0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14}

print( numbers )

 
#numbers.remove(20) Will throw an error

numbers.discard(20) # discard() will not throw an error even if the item not present in the list.