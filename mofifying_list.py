fruits =["apple","orange","strawberry","banana"]

print(fruits) #['apple', 'orange', 'strawberry', 'banana']

fruits.append("melon")
fruits.append("grape")

print(fruits)#['apple', 'orange', 'strawberry', 'banana', 'melon', 'grape']

#Access the list elements using index

print(fruits[2]) #strawberry

fruits[2] = "kiwi" # Modifying the list element

print(fruits) #['apple', 'orange', 'kiwi', 'banana', 'melon', 'grape']

print(fruits[1:4]) #['orange', 'kiwi', 'banana']


fruits[1:4] =["lime"] # #['orange', 'kiwi', 'banana'] replaced with ['lime']

print(fruits) #['apple', 'lime', 'melon', 'grape']']

print(fruits[2]) #melon

fruits[2:] = ["kiwi"] # Inserting elements without removing any element


print(fruits) #['apple', 'lime', 'kiwi']

fruits[:2] =["kiwi"] # Replacing first two elements

print(fruits) #['kiwi', 'kiwi']

fruits =["apple","orange","strawberry","banana"]

 
fruits[:2] = ["lemon","gooseberry","jackfruit"] # Removing all elements from the list

print(fruits) #['lemon', 'gooseberry', 'jackfruit', 'strawberry', 'banana']
