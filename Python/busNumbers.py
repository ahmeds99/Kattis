import sys

antallBusser = int(sys.stdin.readline())
busser = sys.stdin.readline().split()
busser = list(map(int, busser))
sortert = sorted(busser)

resultat = ""
i = 0
while i < len(sortert):
    hjelpeInd = i
    sjekk = 1
    while hjelpeInd < len(sortert) - 1 and sortert[hjelpeInd + 1] == sortert[i] + sjekk:
        sjekk += 1
        hjelpeInd += 1

    if sjekk >= 3:
        if hjelpeInd < len(sortert) - 1:
            resultat += str(sortert[i]) + "-" + str(sortert[i + sjekk - 1]) + " "
        else:
            resultat += str(sortert[i]) + "-" + str(sortert[i + sjekk - 1])
        i += sjekk
    else:
        resultat += str(sortert[i]) + " "
        i += 1

print(resultat)