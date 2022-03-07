import sys


for linje in sys.stdin:
    linje = linje.split()
    oversikt = set()
    antTall = int(linje[0])
    for i in range(1, antTall):
        oversikt.add(str(i))
    
    for i in range(2, len(linje)):
        elem = str(abs(int(linje[i - 1]) - int(linje[i])))
        if elem in oversikt: oversikt.remove(elem)

    if not oversikt:
        print("Jolly")
    else:
        print("Not jolly")
