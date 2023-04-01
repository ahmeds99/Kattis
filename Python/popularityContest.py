import sys 

venner = []
ant_venner, ant_vennskap = [int(x) for x in sys.stdin.readline().split()]

for i in range(ant_venner):
    venner.append(- (i + 1))

for i in range(ant_vennskap):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    venner[a - 1] = venner[a - 1] + 1
    venner[b - 1] = venner[b - 1] + 1

print(*venner)