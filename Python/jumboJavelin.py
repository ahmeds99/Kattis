import sys

rods = int(sys.stdin.readline())
total = 0
for i in range(rods):
    total += int(sys.stdin.readline())

print(total - rods + 1)