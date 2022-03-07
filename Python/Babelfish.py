import sys

fil = open("babelfish.txt")
ordbok = {}

linje = fil.readline()
delopp = linje.split()

while len(delopp) > 0:
    oversatt = delopp[1].strip()
    engelsk = delopp[0].strip()

    ordbok[oversatt] = engelsk

    linje = fil.readline()
    delopp = linje.split()

for lin in fil:
    deler = lin.split()
    if deler[0] in ordbok:
        print(ordbok[deler[0]])
    else:
        print("eh")