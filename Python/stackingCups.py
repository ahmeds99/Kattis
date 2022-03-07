import sys
import bisect

antallKopper = int(sys.stdin.readline())
sortert = []
oversikt = {}

for i in range(antallKopper):
    info = sys.stdin.readline().strip().split()
    if info[0].isnumeric():
        oversikt[int(info[0]) / 2] = info[1]
        bisect.insort(sortert, int(info[0]) / 2)
    else:
        oversikt[int(info[1])] = info[0]
        bisect.insort(sortert, int(info[1]))

for i in range(len(sortert)):
    print(oversikt[sortert.pop(0)])