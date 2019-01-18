import re
n=int(input())
for i in range(n):
    string = input()
    card_starting = re.search(r"^[456]",string)
    seperate = re.match(r"(-?\d{4}){4}$",string)
    consecutive = re.search(r"(.)(-?\1){3,}",string)
    if ( card_starting and seperate  and not consecutive):
        print("Valid")
    else:
        print("Invalid")