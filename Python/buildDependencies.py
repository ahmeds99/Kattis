import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.incoming = set()
        self.outgoing = set()
    
    def __str__(self):
        return str(self.data) + f" Out: {len(self.outgoing)}, In: {len(self.incoming)}"

class Graph:
    def __init__(self, antall):
        # Nøkkelen er noden, verdien er nabonodene, representert i en naboliste
        self.noder = {}
        self.antall = antall

    def lesLinje(self, linje):
        biter = linje.split(":")
        fil = biter[0]
        if fil not in self.noder:
            self.noder[fil] = Node(fil)

        if len(biter) > 1 and biter[1] != "\n":
            v = self.noder[fil]
            for dep in biter[1].split():
                if dep not in self.noder:
                    ny = Node(dep)
                    self.noder[dep] = ny
                else:
                    ny = self.noder[dep]

                v.outgoing.add(ny)
                ny.incoming.add(v)
    
    def ferdigLest(self):
        return set(self.noder.values())

# Prøvde først iterativt, men gjør det heller rekursivt   
def topSort(graph, start, printed):

    if start not in printed:
        print(start)
        printed[start] = start

    for incom in G.noder[start].incoming:
        if incom.data not in printed:
            printed[incom.data] = incom.data
            print(incom.data)

    for incom in G.noder[start].incoming:
        topSort(graph, incom.data, printed)

# antall noder
antNoder = int(sys.stdin.readline())
G = Graph(antNoder)

for i in range(antNoder):
    G.lesLinje(sys.stdin.readline())

graf = G.ferdigLest()
start = sys.stdin.readline().strip()
topSort(graf, start, {})
