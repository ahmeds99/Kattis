import sys

title, cap = sys.stdin.readline().strip().split()
length = len(title)
cap = float(cap)

print(min(length, cap))
