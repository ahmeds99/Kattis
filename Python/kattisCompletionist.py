import sys, heapq, decimal
decimal.getcontext().prec = 2

info = sys.stdin.readline().split()

ulosteProblemer = int(info[0])
minScorePerDag = decimal.Decimal(info[1])

heap = []

for score in sys.stdin.readline().split():
    heapq.heappush(heap, decimal.Decimal(score))

antDager = 1
dagensSum = 0

while heap:
    letteste = heapq.heappop(heap)
    dagensSum += letteste
    if dagensSum > minScorePerDag:
        antDager += 1
        dagensSum = 0

    # print(dagensSum, " antDager", antDager)

print(antDager)