
from collections import defaultdict
# We must declare the data type of value , here it is int
people = defaultdict( int )

people.update({"Bob":45,"Asha":47 })

print( people )

print( people["Asha"])# 47

print( people["Rajeev"]) #0
