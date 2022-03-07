import sys
from collections import defaultdict

info = sys.stdin.readline().split()

graf = defaultdict(lambda: [])

for i in range(int(info[1])):
    deler = sys.stdin.readline().split()

    graf[deler[0]].append(deler[1])
    graf[deler[1]].append(deler[0])

antallOddeGrad = 0
for node in graf:
    if len(graf[node]) % 2 == 1:
        antallOddeGrad += 1

print(antallOddeGrad)