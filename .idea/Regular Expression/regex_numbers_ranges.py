import re

def main():
    import re

    email ="rajeev@gmail.com"


    result = re.match(r"\w{2,10}@",email)
    result = re.match(r"\w{2,10}@\w{2,40}.\w{2,10}",email)

    print( "No match" if result is None else "Match")


main()