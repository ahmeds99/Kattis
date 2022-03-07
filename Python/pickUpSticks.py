import sys
"""
Kjører ikke fort nok.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.incoming = set()
        self.outgoing = set()
    
    def __str__(self):
        return str(self.data) #+ f" Out: {len(self.outgoing)}, In: {len(self.incoming)}"

class Graph:
    def __init__(self, antall):
        # Nøkkelen er noden, verdien er nabonodene, representert i en naboliste
        self.noder = {}
        self.antall = antall

    def lesLinje(self, linje):
        biter = linje.split()
        pinne = biter[0]
        if pinne not in self.noder:
            self.noder[pinne] = Node(pinne)

        v = self.noder[pinne]
        pinneUnder = biter[1]
        if pinneUnder not in self.noder:
            ny = Node(pinneUnder)
            self.noder[pinneUnder] = ny
        else:
            ny = self.noder[pinneUnder]

        v.outgoing.add(ny)
        ny.incoming.add(v)
    
    # def ferdigLest(self):
    #     return set(self.noder.values())

# Prøvde først iterativt, men gjør det heller rekursivt   
def topSort(graph):

    stack = []
    printed = []

    for ver in graph.noder:
        vertex = graph.noder[ver]
        inCount = len(vertex.incoming)
        if inCount == 0:
            stack.append(vertex)
            
    while stack:
        v = stack.pop()
        printed.append(v)

        for nabo in v.outgoing:
            nabo.incoming.discard(v)
            if len(nabo.incoming) == 0:
                stack.append(nabo)

    if len(printed) < G.antall:
        print("IMPOSSIBLE")
    else:
        for node in printed:
            print(node)

# antall noder
deler = sys.stdin.readline().split()
antNoder = int(deler[0])
G = Graph(antNoder)

for i in range(int(deler[1])):
    G.lesLinje(sys.stdin.readline())

# graf = G.ferdigLest()
# for nod in graf:
    # print(nod)
topSort(G)
