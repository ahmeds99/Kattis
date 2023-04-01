import sys

numBoils = int(sys.stdin.readline().strip())

edwardIsRight = False
overlappingNumbers = set()

for i in range(numBoils):
    oversikt = set()
    start, end = sys.stdin.readline().strip().split()
    for j in range(int(start), int(end) + 1):
        oversikt.add(j)

    if i == 0:
        overlappingNumbers.update(oversikt)
    else:
        removeNumbers = set()
        for number in overlappingNumbers:
            if number not in oversikt:
                removeNumbers.add(number)
        overlappingNumbers.difference_update(removeNumbers)


print("edward is right" if not overlappingNumbers else "gunilla has a point")
