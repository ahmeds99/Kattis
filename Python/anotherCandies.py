fil = open("candies.txt")

antallTester = int(fil.readline())
testNr = 0

while testNr != antallTester:
    total = 0
    fil.readline()
    antallBarn = int(fil.readline())

    for i in range(antallBarn):
        total += int(fil.readline())
    
    if total % antallBarn == 0:
        print("YES")
    else:
        print("NO")

    testNr += 1