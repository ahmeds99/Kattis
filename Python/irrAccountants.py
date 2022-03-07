import sys

info = sys.stdin.readline().split()
oversikt = {}
for vare in sys.stdin.readline().split():
    if vare in oversikt:
        oversikt[vare] += 1
    else:
        oversikt[vare] = 1

kategorier = sys.stdin.readline().strip().split()
hyller = {}
for i in range(len(kategorier)):
    katego = sys.stdin.readline().strip().split()
    hyller[katego[0]] = katego[2:]

resultat = []
for kat in hyller:
    for v in hyller[kat]:
        if v in oversikt:
            for i in range(oversikt[v]):
                resultat.append(v)

print(*resultat)