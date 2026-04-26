import re

tag ='<div id="123">Hello</div>'

result = re.match(r"<[^>]+>",tag)

print(result)

result = re.match(r"<[^>]+>[^<>]+",tag)

print( result ) #'<div id="123">Hello'

result = re.match(r"<[^>]+>([^<>]+)</[^>]+>",tag)

print( result ) #<div id="123">Hello</div>

content = result.group(1)

print( content) #Hello

