import sys
from collections import defaultdict

info = sys.stdin.readline().split()

liste = sys.stdin.readline().split()
liste = [int(x) for x in liste]

ordbok = defaultdict(lambda: (0, sys.maxsize))
for i in range(int(info[0])):
    ordbok[liste[i]] = (ordbok[liste[i]][0] + 1, ordbok[liste[i]][1])
    if i < ordbok[liste[i]][1]:
        ordbok[liste[i]] = (ordbok[liste[i]][0], i)

liste.sort(key=lambda x: (-ordbok[x][0], ordbok[x][1]))
print(*liste)