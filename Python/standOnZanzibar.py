import sys

antCaser = int(sys.stdin.readline())

for i in range(antCaser):
    info = sys.stdin.readline().split()
    total = 0
    fjorÅret = 1
    for i in range(len(info) - 1):
        if int(info[i]) > fjorÅret * 2:
            total += int(info[i]) - fjorÅret * 2
        fjorÅret = int(info[i])
    print(total)
    