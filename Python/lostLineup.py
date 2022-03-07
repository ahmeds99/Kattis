import sys, heapq

class KoObjekt:
    def __init__(self, koNr, indeks):
        self.koNr = koNr
        self.indeks = indeks
    
    def __lt__(self, annen):
        return self.koNr < annen.koNr

antallIKo = int(sys.stdin.readline())
heap = []
info = sys.stdin.readline().split()
info = [int(n) for n in info]

for i in range(len(info)):
    heapq.heappush(heap, KoObjekt(info[i], i + 2))

print(1, end=" ")
while (len(heap) > 0):
    print(heapq.heappop(heap).indeks, end=" ")
print()