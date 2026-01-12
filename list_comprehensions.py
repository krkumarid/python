animals1 = ["dog","goat","sloth","tiger"]
"""
animals2  = animals1
del animals2[1]

print( animals1) #['dog', 'sloth', 'tiger']
print( animals2) #['dog', 'sloth', 'tiger']

"""

"""
animals3 = animals1.copy()
del animals3[1]

print( animals1) #['dog', 'goat', 'sloth', 'tiger']
print( animals3) #['dog', 'sloth', 'tiger'] 

"""

""" animals4  = [ animl for animl in animals1 ]

print( animals4) #['dog', 'goat', 'sloth', 'tiger']
"""
animals5  = [ animl.upper() for animl in animals1 ]

print( animals5) #['DOG', 'GOAT', 'SLOTH', 'TIGER']

lengths = [ len(animl) for animl in animals1 ]

print( lengths) #[3, 4, 5, 5] 
squared = [ num**2 for num in range(1,11) ]
print( squared) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]