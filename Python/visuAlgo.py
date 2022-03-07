import sys
from collections import defaultdict
import heapq

def dijkstra(graf, start, slutt):
    q = []
    heapq.heappush(q, (0, start))
    D = defaultdict(lambda: float("inf"))
    stier = defaultdict(lambda: 0)
    D[start] = 0
    stier[start] = 1

    while q:
        kost, v = heapq.heappop(q)
        for nabo in graf[v]:
            c = kost + nabo[1]
            if c < D[nabo[0]]:
                D[nabo[0]] = c
                heapq.heappush(q, (c, nabo[0]))
                stier[nabo[0]] = stier[v]
            elif c == D[nabo[0]]:
                stier[nabo[0]] += stier[v]
            
        if v == slutt:
            return stier[slutt]
    return stier[slutt]

info = sys.stdin.readline().split()
graf = defaultdict(lambda: [])

# Antall kanter
for _ in range(int(info[1])):
    biter = sys.stdin.readline().split()
    graf[biter[0]].append((biter[1], int(biter[2])))

start, slutt = sys.stdin.readline().split()
kortesteStier = dijkstra(graf, start, slutt)
print(kortesteStier)