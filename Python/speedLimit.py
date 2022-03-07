import sys 

fil = open("speedLimit.txt")

for linje in fil:
    antallLinjer = int(linje)
    if antallLinjer > 0:
        antallMil = 0

        forrigeTime = 0
        for i in range(antallLinjer):
            info = fil.readline().split()
            miles = int(info[0])
            timer = int(info[1])
            nåværendeTime = timer

            if forrigeTime != 0:
                timer -= forrigeTime
                forrigeTime = nåværendeTime
            else:
                forrigeTime = timer

            antallMil += miles * timer 
        
        print(antallMil, " miles")