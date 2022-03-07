import sys

info = sys.stdin.readline().split(" ")

while info[0] != "0" and info[1] != "0":
    jackAntall = int(info[0])
    jillAntall = int(info[1])
    jackCd = {}
    antFelles = 0

    for i in range(jackAntall):
        katalogNr = int(sys.stdin.readline())
        jackCd[katalogNr] = katalogNr

    for j in range(jillAntall):
        katNr = int(sys.stdin.readline())
        if katNr in jackCd:
            antFelles += 1

    print(antFelles)
    info = sys.stdin.readline().split()