import sys

maks = 1000
antallForsøk = 1
nedreGrense = 0
øvreGrense = 1001

gjett = int(maks / 2)
print(gjett, flush=True)

respons = sys.stdin.readline().strip()
while antallForsøk < 10:
    if respons == "correct":
        break
    
    elif respons == "higher":
        nedreGrense = gjett
        if gjett > 1000:
            gjett = 1000
        antallForsøk += 1

    else:
        øvreGrense = gjett
        if gjett < 1:
            gjett = 1
        antallForsøk += 1
    
    gjett = int(nedreGrense + (øvreGrense - nedreGrense) / 2)

    print(gjett, flush=True)
    respons = sys.stdin.readline().strip()

