def checkSeq(charA: list, i: int):
    if len(charA)>2 and charA[2]=="u":
        if charA[1] == "u" and charA[0] == "-":
            if i == 6:
                print("no")
                exit()
            else:
                return "d"

    if len(charA)>1:
        if charA[1] == "u" and charA[0] == "-":
            if i != 6: 
                print("no")
                exit()
            else:
                return "t"
        elif charA[0] == "-" and charA[1] == "-":
            return "s"
    print("no")
    exit()


l = list(input())
a = 0
b = 3
n = 1
while(n<7):
    x = checkSeq(l[a:b],n)
    if n == 6:
        break
    if x == "d":
        a += 3
        b += 3
    else: 
        a += 2
        b += 2
    n += 1
if a+2<len(l):
    print("no")
else:
    print("yes")
