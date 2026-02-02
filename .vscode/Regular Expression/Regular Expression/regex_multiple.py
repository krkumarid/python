import re

def main():
    text ="drooooool"
    result = re.match("dr.*l",text)

    if result is None:
        print("Not matching")
    else:
        print(result.group())

main()