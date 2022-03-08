import sys

antCaser = int(sys.stdin.readline())

for i in range(antCaser):
    ulikeByer = set()
    for i in range(int(sys.stdin.readline())):
        ulikeByer.add(sys.stdin.readline())
    print(len(ulikeByer))