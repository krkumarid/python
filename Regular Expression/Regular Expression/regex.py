import re

def main():
    text ="dig"
    result = re.match("dog",text)
    print(result)
    print( result is not None)
    result = re.match("dd.g",text)# dd.g is not matching with text so it will print False
    print(result is not None) # . is a wild char in regular expression.


main()
