import bisect
import math

n = int(input())
sortert = []

for _ in range(n):
    bisect.insort(sortert, int(input()), key=lambda x: -x)

groups = math.ceil(n / 3)
total = 0
for i in range(len(sortert)):
    if (i + 1) % 3 != 0:
        total += sortert[i]

print(total)
