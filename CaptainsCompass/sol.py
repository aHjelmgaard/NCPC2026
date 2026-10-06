
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

instructions = []

if x1 == x2:
    if y1 < y2:
        instructions.append("N")
    else:
        instructions.append("S")
elif y1 == y2:
    if x1 < x2:
        instructions.append("E")
    else:
        instructions.append("W")
elif abs(x1-x2) == abs(y1-y2):
    if x1 < x2:
        if (y1 < y2):
            instructions.append("NE")
        else:
            instructions.append("SE")
    else:
        if (y1 < y2):
            instructions.append("NW")
        else:
            instructions.append("SW")
else:
    s = ""
    if abs(x1-x2) < abs(y1-y2):
        if y1 < y2:
            s = "N"
        else:
            s = "S"
        instructions.append(s)
        if x1<x2:
            instructions.append(s+"E")
        else:
            instructions.append(s+"W")
    else:
        if x1 < x2:
            s = "E"
        else:
            s = "W"
        instructions.append(s)
        if y1<y2:
            instructions.append("N"+s)
        else:
            instructions.append("S"+s)

for x in instructions:
    print(x)