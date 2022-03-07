import sys

# IKKE FERDIG

info = sys.stdin.readline().strip()
antallD = info.count("D")

forrige = info[0]
antall = 0
for do in info[1:]:
    if do != forrige:
        antall += 1
    forrige = do

print(antall)