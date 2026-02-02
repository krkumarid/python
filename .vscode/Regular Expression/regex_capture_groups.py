"""
Docstring for .idea.Regular Expression.regex_numbers_and_words
\w Matches alphanumeric characters
+  matches one or more as many as possible.
\w :Matches one or more, as many as possible (\w+ one or more alpha numeric characters)
\s: match a spece (\s+  more space )
\d: match a digit (\d+ one or more more digits)
"""

import re

text ="The temperature is: 37"


result = re.match(r".*:\s*(\d+)",text)

print( "No match" if result is None else f"'{ result.group(0)}'")
print( "No match" if result is None else f"'{ result.group(1)}'")