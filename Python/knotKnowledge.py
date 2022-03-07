import sys

antallKnuter = int(sys.stdin.readline())

skalKunne = {}
for tall in sys.stdin.readline().split():
    skalKunne[tall] = tall

for kan in sys.stdin.readline().split():
    skalKunne.pop(kan)

for ikkeKan in skalKunne:
    print(ikkeKan)