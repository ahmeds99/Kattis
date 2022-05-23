import sys

info = sys.stdin.readline()
tall = int(info)

if tall < 149:
    print(99)
else:
    lastTwo = info[len(info) - 3:]
    if int(lastTwo) >= 49:
        print(tall + (99 - int(lastTwo)))
    else:
        print(tall - (int(lastTwo) + 1))