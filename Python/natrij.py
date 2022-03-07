import sys

nåværendeTid = sys.stdin.readline().split(":")
eksplosjon = sys.stdin.readline().split(":")
resultat = ""

nvTime = int(nåværendeTid[0])
eksTime = int(eksplosjon[0])

if nvTime > eksTime:
    timer = 24 - nvTime + eksTime
else:
    timer = eksTime - nvTime

nvMin = int(nåværendeTid[1])
eksMin = int(eksplosjon[1])

if nvMin > eksMin:
    min = 60 - nvMin + eksMin
    if timer != 0:
        timer -= 1
else:
    min = eksMin - nvMin

nvSek = int(nåværendeTid[2])
eksSek = int(eksplosjon[2])

if nvSek > eksSek:
    sek = 60 - nvSek + eksSek
    if min == 0:
        timer -= 1
        min = 59
    else:
        min -= 1
else:
    sek = eksSek - nvSek

if timer == 0:
    resultat += "00:"
elif len(str(timer)) == 1:
    resultat += "0" + str(timer) + ":"
else:
    resultat += str(timer) + ":"

if min == 0:
    resultat += "00:"
elif len(str(min)) == 1:
    resultat += "0" + str(min) + ":"
else:
    resultat += str(min) + ":"

if sek == 0:
    resultat += "00"
elif len(str(sek)) == 1:
    resultat += "0" + str(sek) 
else:
    resultat += str(sek) 

if nåværendeTid == eksplosjon:
    print("24:00:00")
else:
    print(resultat)