import sys

info = sys.stdin.readline().split()
flaskerVedStart = int(info[0])
flaskerFunnet = int(info[1])
flaskerForNyBrus = int(info[2])

total = flaskerVedStart + flaskerFunnet
brusDrukket = 0
while (total - flaskerForNyBrus) >= 0:
    brusDrukket += 1
    total -= flaskerForNyBrus
    total += 1

print(brusDrukket)