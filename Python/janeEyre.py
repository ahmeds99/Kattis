import sys
import heapq

data = sys.stdin.readline().split()
antBøker = int(data[0])
bøkerFraVenner = int(data[1])
siderJaneEyre = int(data[2])
tidGått = 0

heap = []
venneHeap = []

heapq.heappush(heap, ("Jane Eyre", siderJaneEyre))

for i in range(antBøker):
    info = sys.stdin.readline().strip().split('\"')
    heapq.heappush(heap, (info[1], int(info[2])))

for j in range(bøkerFraVenner):
    info = sys.stdin.readline().strip().split('\"')
    heapq.heappush(venneHeap, (int(info[0]), info[1], int(info[2])))

nåværendeBok = heapq.heappop(heap)
while nåværendeBok[0] != "Jane Eyre":
    tidGått += nåværendeBok[1]
    while venneHeap and venneHeap[0][0] <= tidGått:
        fjernet = heapq.heappop(venneHeap)
        heapq.heappush(heap, (fjernet[1], fjernet[2]))
    nåværendeBok = heapq.heappop(heap)

print(tidGått + siderJaneEyre)
