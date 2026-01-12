animals1 = ("dog", "cat", "mouse")
animals2 = ("elephant", "tiger", "lion")

fruits1 = ["apple", "orange"]
fruits2 = ["strawberry", "melon", "blueberry", "grape"]

value = 5;
value+=3
print(value)

print( id(animals1))
animals1 += animals2
print( id(animals1)) # New memory address since tuples are immutable

print( animals1) #('dog', 'cat', 'mouse', 'elephant', 'tiger', 'lion')
print( len( animals1)) #6


print(id(fruits1))
fruits1 += fruits2
print(id(fruits1)) # Same memory address since lists are mutable
print(len(fruits1)) #6
print( fruits1) #['apple', 'orange', 'strawberry', 'melon', 'blueberry', 'grape']


