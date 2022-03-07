import sys

info = sys.stdin.readline().split()
harEgget = 0
stack = []

kommandoer = sys.stdin.readline().split()
i = 0
while i < len(kommandoer):
    if kommandoer[i] != "undo":
        stack.append(kommandoer[i])
    else:
        i += 1
        for j in range(int(kommandoer[i])):
            stack.pop()
    i += 1

for tall in stack:
    harEgget += int(tall)

print(harEgget % int(info[0]))