import sys

kø = []
antPersoner = int(sys.stdin.readline())

for _ in range(antPersoner):
    kø.append(sys.stdin.readline().strip())

antKommandoer = int(sys.stdin.readline())

for _ in range(antKommandoer):
    kommando = sys.stdin.readline().strip().split()

    if kommando[0] == "cut":
        kø.insert(kø.index(kommando[2]), kommando[1])
    
    elif kommando[0] == "leave":
        kø.remove(kommando[1])

for navn in kø: print(navn)