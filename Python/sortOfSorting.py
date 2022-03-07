import sys

antall = int(sys.stdin.readline())

while antall != 0:
    navn = []
    for i in range(antall):
        navn.append(sys.stdin.readline())
    
    navn = sorted(navn, key=lambda x:x[:2])
    for n in navn:
        print(n)
    
    print()
    antall = int(sys.stdin.readline())