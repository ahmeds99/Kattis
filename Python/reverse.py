import sys

stack = []

for i in range(int(sys.stdin.readline())):
    stack.append(sys.stdin.readline().strip())

while stack:
    print(stack.pop())