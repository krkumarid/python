import re


def main():
    text ="""
         one
         two
         three
    """
    result = re.search(r"two",text) # Search tart the matching not from the begining like match () 'two'
    result = re.search(r"t.*e",text) #'three'

    if result is None:
        print("No match")
    else:
        print(f"Match : '{result.group(0)}'")

main()

