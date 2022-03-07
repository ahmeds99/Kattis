import sys

antCaser = int(sys.stdin.readline())

for i in range(antCaser):
    info = sys.stdin.readline().split()
    ikkeReklame = int(info[0])
    totalKostnad = int(info[1]) - int(info[2])
    
    if ikkeReklame == totalKostnad:
        print("does not matter")
    elif ikkeReklame > totalKostnad:
        print("do not advertise")
    else:
        print("advertise")