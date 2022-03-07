import sys
"""
IKKE RASK NOK
"""

antCaser = int(sys.stdin.readline())

for i in range(antCaser):
    kommandoer = sys.stdin.readline().strip()
    størrelse = int(sys.stdin.readline())
    liste = []
    reversert = False
    error = False

    tall = sys.stdin.readline().strip()
    if len(tall) > 2:
        liste = tall[1:len(tall)-1].split(",")
  
    for kom in kommandoer:
        if kom == "R":
            reversert = not reversert
        else:
            if len(liste) == 0:
                error = True
                break
            if not reversert:
                liste.pop(0)
            else:
                liste.pop()

    if error:
        print("error")
    elif reversert:
        print(str(liste[::-1]).replace(" ", "").replace("'", ""))
    else:
        print(str(liste).replace(" ", "").replace("'",""))