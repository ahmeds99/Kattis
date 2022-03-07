import sys
import bisect

antTurer = int(sys.stdin.readline())
oversikt = {}

for i in range(antTurer):
    info = sys.stdin.readline().split()

    if info[0] in oversikt:
        bisect.insort_left(oversikt[info[0]], int(info[1]))
    else:
        oversikt[info[0]] = [int(info[1])]

antQueries = int(sys.stdin.readline())
for i in range(antQueries):
    land, ind = sys.stdin.readline().split()

    print(oversikt[land][int(ind) - 1])