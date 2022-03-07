
def administrerSaldo(filnavn):
    saldoOversikt = {}

    fil = open(filnavn)
    antallMennesker = int(fil.readline()[0])

    restart = 0
    
    for linje in fil:
        biter = linje.split()
        if biter[0] == "SET":
            saldoOversikt[biter[1]] = int(biter[2])
        
        elif biter[0] == "PRINT":
            if biter[1] in saldoOversikt:
                print(saldoOversikt[biter[1]])
            else:
                print(restart)
        
        else: # reset saldoene til hver person til oppgitt verdi
            restart = biter[1]
            saldoOversikt = {}

administrerSaldo("AccountingTest.txt")
