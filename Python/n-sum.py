import sys

sys.stdin.readline()

info = sys.stdin.readline().split()
sum = 0

for tall in info:
    sum += int(tall)

print(sum)