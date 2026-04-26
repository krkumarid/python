import re

def main():
    text ="""
         one
         two
         three
    """
    print( re.match("\s*one\s*two",text,re.DOTALL))
    print()
    print( re.match(".*two",text,re.DOTALL))
main()