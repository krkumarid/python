
import re

def main():
    text = "zigzag"
    result = re.match("z.*",text) #Match:zigzag

    print( "No match" if result is None else f"Match:{result.group()}" )

    text = "zigzag"
    result = re.match("z.*?g",text) #Match:zig

    print( "No match" if result is None else f"Match:{result.group()}" )

    text = "zigzag"
    result = re.match("z.*?",text) #Match:z

    print( "No match" if result is None else f"Match:{result.group()}" )

    text = "zigzag"
    result = re.match("z.*?$",text) #Match:zigzag

    print( "No match" if result is None else f"Match:{result.group()}" )


main()