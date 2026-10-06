from collections import deque

n = int(input())

times = list(map(int, input().split()))
solutions = set()

for xy in times[1::]:
    s = xy-times[0]
    qF = deque()
    qF.append(times[0])
    x = 1
    valid = True
    while x< n and valid:
        if len(qF)==0:
            qF.append(times[x])
            x+=1
            continue
        dif = times[x]-qF[0]
        if dif>s:
            valid = False
        elif dif<s:
            qF.append(times[x])
        elif dif==s:
            qF.popleft()
        x += 1
    if valid and len(qF)==0 and s != 0:
        solutions.add(s)

print(len(solutions))
for x in solutions:
    print(x)
            