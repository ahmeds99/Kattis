import sys

megaByte = int(sys.stdin.readline())
total = megaByte

for i in range(int(sys.stdin.readline())):
    total += (megaByte - int(sys.stdin.readline()))

print(total)