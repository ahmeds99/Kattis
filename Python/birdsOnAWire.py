
fil = open("birdsTest.txt")

biter = fil.readline().split()
lengde = int(biter[0])
avstand = int(biter[1])
antallSittende = int(biter[2])

if lengde == 0:
    print(0)

else:
    if antallSittende == 0:
        print(int((lengde - 12) / avstand + 1))
    
    else:
        opptatt = [0 for i in range(antallSittende)]
        for i in range(antallSittende):
            posisjon = int(fil.readline())
            opptatt[i] = posisjon

        opptatt.sort()

        venstre = opptatt[0] - 6
        høyre = lengde - 6 - opptatt[-1]
        plassTil = 0

        plassTil += (venstre / avstand) + (høyre / avstand)

        for i in range(antallSittende - 1):
            mellom = opptatt[i + 1] - opptatt[i]
            plassTil += (mellom / avstand) - 1

        print(plassTil)