fruits =["apple","orange","banana"]
animals =["dog","cat","goat"]

for i, item in enumerate(fruits):
    print( i, item )

#Zip functiom
for fruit, animal in zip( fruits, animals):
    print( fruit, animal)