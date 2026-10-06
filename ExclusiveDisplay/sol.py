
import operator



dictionary = {
    "1110111":0,
    "0010010":1,
    "1011101":2,
    "1011011":3,
    "0111010":4,
    "1101011":5,
    "1101111":6,
    "1010010":7,
    "1111111":8,
    "1111011":9
    }

a = [[] for _ in range(7)]
for i in range(7):
    line = input()
    if i == 0:
        v = line[1]
        if v == "#":
            a[0] = "1"
        else:
            a[0] = "0"
    elif i == 1:
        v = line[0]
        w = line[3]
        if v == "#":
            a[1] = "1"
        elif v == ".":
            a[1] = "0"
        if w == "#":
            a[2] = "1"
        elif w == ".":
            a[2] = "0"
    elif i == 3:
        v = line[1]
        if v == "#":
            a[3] = "1"
        else:
            a[3] = "0"
    elif i == 4:
        v = line[0]
        w = line[3]
        if v == "#":
            a[4] = "1"
        elif v == ".":
            a[4] = "0"
        if w == "#":
            a[5] = "1"
        elif w == ".":
            a[5] = "0"
    elif i == 6:
        v = line[1]
        if v == "#":
            a[6] = "1"
        else:
            a[6] = "0"
    else:
        continue

b = str(''.join(a))
c = dictionary.get(b)
out = ""
results = []
if c is not None:
    results.append(str(c))
    
else:  
    for k,v in dictionary.items():
        s = ""
        for l in range(7):
            if k[l] == b[l]:
                s += "0"
            else:
                s+="1"
            
                  
        res = dictionary.get(s)
        
        if res is None:
            continue
        if(res != 0):
            results.append(f"{res}{v}")


out = sorted(results)
if len(out) == 0:
    print("impossible")
else:
    y = ""
    for i in out:
        y += i + " "

    print(y.strip())