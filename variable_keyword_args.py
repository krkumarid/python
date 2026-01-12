def add_description(**description):
    print(type( description))
    # print( description)

    for prop in description:
        print( prop,": ", description[prop] )


def main():
   add_description( height=180, weight=90, eyes="blue")
   add_description( trouser="black", beard=True)
   add_description( sex="male", height=170)



main()