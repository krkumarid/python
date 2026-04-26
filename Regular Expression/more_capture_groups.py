import re

email ="one.two.three.four@example.com"

result = re.match(r"((?:\w+\.)*)\w+@\w+\.\w+",email )

if result is None:
    print( "No match")
else:
    print( result.group(1)) #one.two.three.
    print( result.group(0)) #one.two.three.four@example.com
    print( result.groups()) #('one.two.three.',)

