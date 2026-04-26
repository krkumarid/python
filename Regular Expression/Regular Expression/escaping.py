
import re
text ="-\n-"

print(text) # -
            # -

#The python treated the \n as new line
#If we are putting it as a raw string, the python will skip the escape character

text =r"-\n-"

print( text ) #-\n-

result = re.match(r"-\\n-",text)

print( result) #<re.Match object; span=(0, 4), match='-\\n-'>