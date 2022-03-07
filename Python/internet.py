from collections import deque
import sys
import array as arr

def BFS(G, s):
    queue = deque()
    queue.append(s)
    besøkte[int(s)] = True

    while len(queue) > 0:
        s = queue.popleft()

        for nabo in noder[s]:
            if not besøkte[int(nabo)]:
                besøkte[int(nabo)] = True
                queue.append(nabo)


info = sys.stdin.readline().split()
antNoder = int(info[0])
kanter = int(info[1])
besøkte = arr.array("b", [False for i in range(antNoder + 1)])

noder = {}
for i in range(antNoder):
    noder[i + 1] = set()

for i in range(kanter):
    deler = sys.stdin.readline().split()
    a = int(deler[0])
    b = int(deler[1])

    noder[a].add(b)
    noder[b].add(a)

BFS(noder, 1)
out = []
notConnected = False
for i in range(1, antNoder + 1):
    if not besøkte[i]:
        notConnected = True
        out.append(str(i) + "\n")
        # print(out)

if not notConnected:
    print("Connected")
else:
    print("".join(out), end="")
