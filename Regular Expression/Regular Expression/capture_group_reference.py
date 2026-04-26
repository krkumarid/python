import re

tag ='<div id="123">Hello</div>'

result = re.match(
    r"""
        <(div)\s+                #Match opening tag
        id="(\w+)"             # Match id attribute
        >                      # End of opening tag
        ([^<>]+)               # Match contents of tag
        </div>                 # Closing div tag
    """,
    tag, re.VERBOSE)
print( result)
tag,id, content = result.groups()

print( tag,id,content)

i =0
while i!=0:
    i=i=1
else:
    i=i+1
print(i)
