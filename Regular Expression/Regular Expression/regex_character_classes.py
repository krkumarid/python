import re

print( re.match(r"[abc]+","abc")) #<re.Match object; span=(0, 3), match='abc'>

print( re.match(r"[abc]","abc")) #<re.Match object; span=(0, 1), match='a'>

print( re.match(r"[a-z]+","abcd")) #<re.Match object; span=(0, 4), match='abcd'>

print(re.match(r"[a-b]+","abcd")) #<re.Match object; span=(0, 2), match='ab'>

print(re.match(r"[a-z\d]+","abc3d")) 

print(re.match(r"[a-z\d\-\.]+","a-b.c3d")) 

#First character should be a lower case letter
# . or -
#@
print(re.match(r"[a-z]","john.purcell@caveofprogramming.com")) 
print(re.match(r"[a-z][a-z\-\.]+","john.purcell@caveofprogramming.com"))

print(re.match(r"([a-z][a-z\-\.]+)@","john.purcell@caveofprogramming.com"))

print(re.match(r"([a-z][a-z\-\.]+)@(\w+)\.(\w+)","john.purcell@caveofprogramming.com"))


result = re.match(r"([a-z][a-z\-\.]+)@(\w+)\.(\w+)","john.purcell@caveofprogramming.com")

name,domain,suffx = result.groups()
print( name,domain,suffx )