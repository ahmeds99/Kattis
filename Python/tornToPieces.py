from collections import deque
import sys


foreldre = {}
noder = {}
visitedNodes = {}

path = []
def DFS(node):
    if node not in noder:
        return False
    
    visitedNodes[node] = node
    if node == start:
        return True

    for nabo in noder[node]:
        if nabo in visitedNodes:
            continue
        foreldre[nabo] = node
        if DFS(nabo):
            return True
    return False

antall = int(sys.stdin.readline())
# G = Graph(antall)
for i in range(antall):
    deler = sys.stdin.readline().split()
    node = deler[0]
    if node not in noder:
        foreldre[node] = ""
        noder[node] = set()

    for nabo in deler[1:]:
        if nabo not in noder:
            foreldre[nabo] = ""
            noder[nabo] = set()
        
        noder[node].add(nabo)
        noder[nabo].add(node)


info = sys.stdin.readline().split()
start = info[0]
destinasjon = info[1]
funn = DFS(destinasjon)

if funn:
    første = start
    while (første != ""):
        print(første, end=" ")
        første = foreldre[første]

else:
    print("no route found")