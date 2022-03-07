import sys
from collections import deque

kø = deque()

antTall = int(sys.stdin.readline())
info = sys.stdin.readline().split()
umulig = False

antTrekk = 0
totalLengde = len(info)

for i in range(len(info)):
    if len(kø) > totalLengde:
        umulig = True
        break
    if kø and kø[0] == info[i]:
        antTrekk += 1
        kø.popleft()
    else:
        kø.appendleft(info[i])
        antTrekk += 1

if umulig or len(kø) > 0:
    print("impossible")
else:
    print(antTrekk)
    
