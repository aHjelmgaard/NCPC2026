def checkSeq(a, b, c, i: int):
    if c == "u":
        if b == "u" and a == "-":
            if i == 6:
                print("no")
                exit()
            else:
                return "d"

    if a == "-" and b == "u":
        if i == 6: 
            return "t"
        else:
            print("no")
            exit()
    elif a == "-" and b == "-":
        return "s"
    print("no")
    exit()


l = list(input())
m = len(l)
y = 0
n = 1
while(n<7):
    a = "null"
    b = "null"
    c = "null"
    if y<m:
        a = l[y]
    if y+1<m:
        b = l[y+1]
    if y+2<m:
        c = l[y+2]
    x = checkSeq(l[a:b],n)
    if x == "d":
        y += 3
    else: 
        y += 2
    n += 1
print("yes")
