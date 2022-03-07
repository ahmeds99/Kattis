import sys

antall = int(sys.stdin.readline())
caseNr = 1
while antall != 0:
    print("SET", caseNr)
    stack = []
    først = True
    antallBak = 1
    for i in range(antall):
        navn = sys.stdin.readline()
        if først:
            print(navn)
            først = False
        else:
            stack.append(navn)
            først = True
    
    while stack:
        print(stack.pop())

    caseNr += 1
    antall = int(sys.stdin.readline())
