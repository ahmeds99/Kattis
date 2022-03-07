import sys
from collections import defaultdict

"""
IKKE FERDIG
"""

def sammenhengendeKomponenter(graf):
    besøkteNoder = {}
    komponenter = []

    for node in graf:
        if node not in besøkteNoder:
            temp = []
            komponenter.append(DFS(graf, temp, node, besøkteNoder))
    
    return komponenter

def DFS(graf, antallIKomponent, node, besøkteNoder):
    stack = [node]

    while stack:
        nod = stack.pop()
        if nod in besøkteNoder:
            continue
        antallIKomponent.append(nod)
        besøkteNoder[nod] = nod

        for nabo in graf[nod]:
                stack.append(nabo)

    return antallIKomponent

# Antall byer
for _ in range(int(sys.stdin.readline())):
    antNoder = int(sys.stdin.readline())
    graf = defaultdict(lambda: [])

    antKanter = int(sys.stdin.readline())
    for _ in range(antKanter):
        kant = sys.stdin.readline().split()
        graf[kant[0]].append(kant[1])
        graf[kant[1]].append(kant[0])
    
    print(len(sammenhengendeKomponenter(graf)) - 1)