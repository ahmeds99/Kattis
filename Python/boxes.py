import sys

class Node:
    def __init__(self):
        self.indeks = None
        self.barn = []

skog = {}
antallBokser = int(sys.stdin.readline())
boksen = sys.stdin.split(" ")

for i in range(1, len(boksen) + 1):
    if boksen[i] == 0:
        skog{boksen[i]} == 