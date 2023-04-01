import sys

numCaser = int(sys.stdin.readline().strip())
daysSet = set()
for i in range(int(numCaser)):
    days = sys.stdin.readline().strip().split()
    start = int(days[0])
    end = int(days[1])

    for i in range(start, end + 1):
        daysSet.add(i)

print(len(daysSet))
