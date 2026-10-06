n = int(input())

hermits = []
for _ in range(3):
    hermits.append(int(input()))

hermits_sorted = sorted(hermits)

fewest = hermits_sorted[0]

total = fewest + n

if (total < hermits_sorted[1]):
    print(total)
else:
    print("impossible")
