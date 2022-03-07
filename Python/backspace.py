import sys

tekst = sys.stdin.readline()

kø = []
posisjon = 0
for i in range(len(tekst)):
    if tekst[i] != "<":
        kø.append(tekst[i])
    # hvis tegnet er '<', og vi kan poppe fra køen
    elif len(kø) != 0:
        kø.pop()

resultat = ""
while len(kø) != 0:
    resultat += kø[0]
    kø.pop(0)

print(resultat)