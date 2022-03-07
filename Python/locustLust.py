import sys, bisect

def nesteKollisjon(første, andre, nesteFørste, nesteAndre):
    # nesteFørste = start + første
    # nesteAndre = start + andre
    # print(nesteAndre, nesteFørste)
    if nesteFørste == nesteAndre:
        return nesteFørste

    elif nesteFørste < nesteAndre:
        return nesteKollisjon(første, andre, nesteFørste + første, nesteAndre)
    
    else:
        return nesteKollisjon(første, andre, nesteFørste, nesteAndre + andre)

antallCaser = int(sys.stdin.readline())
minste = sys.maxsize
for i in range(antallCaser):
    info = sys.stdin.readline().split()
    år = int(info[0])
    første = int(info[1])
    andre = int(info[2])
    nesteFørste = år + første
    nesteAndre = år + andre
    tall = nesteKollisjon(første, andre, nesteFørste, nesteAndre)
    
    if tall < minste:
        minste = tall

print(minste)