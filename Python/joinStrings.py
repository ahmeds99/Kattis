fil = open("joinStrings.txt")

antallOrd = int(fil.readline())
alleOrd = []

for i in range(antallOrd):
    alleOrd.append(fil.readline().split()[0])

for linje in fil:
    biter = linje.split()
    førsteInd = int(biter[0]) - 1
    andreInd = int(biter[1]) - 1

    alleOrd[førsteInd] = alleOrd[førsteInd] + alleOrd[andreInd]
    alleOrd[andreInd] = ""

print(alleOrd[førsteInd])