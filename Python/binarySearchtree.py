import sys

class Node:
    def __init__(self, verdi):
        self._verdi = verdi
        self.venstre = None
        self.høyre = None
    
    def settVerdi(self, ny):
        self._verdi = ny
    
    def hentVerdi(self):
        return self._verdi

    def __str__(self):
        return str(self._verdi)
    
nåværendeVerdi = 0
def settInn(node, verdi):
    global totalDybde
    if node == None:
        node = Node(verdi)
        print(totalDybde)
    elif verdi < node.hentVerdi():
        totalDybde += 1
        node.venstre = settInn(node.venstre, verdi)
    elif verdi > node.hentVerdi():
        totalDybde += 1
        node.høyre = settInn(node.høyre, verdi)
    return node

totalDybde = 0
antallTall = int(sys.stdin.readline())
rot = settInn(None, int(sys.stdin.readline()))

for linje in sys.stdin:
    tall = int(linje)

    ny = settInn(rot, tall)
    
