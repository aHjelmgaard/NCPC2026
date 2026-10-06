def convert(s):
    if s=="u":
        return (0,1)
    if s=="r":
        return (1,0)
    if s=="d":
        return (0,-1)
    if s == "l":
        return (-1, 0)

def rotate(s):
    if s=="u":
        return "l"
    if s=="r":
        return "u"
    if s=="d":
        return "r"
    if s == "l":
        return "d"

path = ["r","u","l","u","l","d","l","u"]
#make path
n = int(input())
while(len(path)<n):
    path1 = []
    for x in range(len(path)-1,-1, -1):
        path1.append(rotate(path[x]))
    path.extend(path1)

start = (0,0)
y = 0
while y < n:
    nextStep = convert(path[y])
    start = (start[0]+nextStep[0], start[1]+nextStep[1])
    y+=1
print(start[0], start[1])