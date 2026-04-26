import re


def main():
    text ="""
         one
         two
         three
    """
    print( re.match("\s*one\s*two",text,re.DOTALL))
    print()
    result =  re.match("(.*two)",text,re.DOTALL)

    result =  re.match("(.*?two.*?)",text,re.DOTALL)

    result =  re.match("(.*?two.*?)$",text,re.DOTALL)

    result =  re.match("(.*?two.*?)$",text,re.DOTALL | re.MULTILINE )  # End  of the line matching

    """
    Match : '
         one
         two'
    
    """

    if result is None:
        print("No match")
    else:
        print(f"Match : '{result.group(1)}'")
   # print(0)
   # x=2
   # y=4
   # x =x//y
   # print(x)
   # y=y//x
   # print(y)
main()

