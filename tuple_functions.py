numbers1 = 1,2,3,2,4,3,2

print( len(numbers1)) #6
# Minimum  value in a tuple
print( min(numbers1)) #1
# Maximum value in a tuple
print( max(numbers1)) #4
# Count of an element in a tuple
print( numbers1.count(2)) #2
index = numbers1.index(3) # Index of first occurrence of an element
print( index) #2
#Adding elements to a tuple - we cannot add elements to a tuple as it is immutable, but we can concatenate two tuples to create a new tuple
print(numbers1+(10,20,10)) #(1, 2, 3, 2, 4, 3, 2, 10, 20, 10)
print( numbers1) #(1, 2, 3, 2, 4, 3, 2) -> original tuple remains unchanged, iT is immutable.

#Multiplying a tuple

print( (1,2,3)*3) #(1, 2, 3, 1, 2, 3, 1, 2, 3)