people ={ 
        "Al":["Running","Programing"],
        "Raj":["Hiking","Reading","writing"],
}

print( people["Raj"][1]) #Reading

for name,hobboies in people.items():
    print( name)
    print("=================")
    for hobby in hobboies:
        print( hobby )
    print()