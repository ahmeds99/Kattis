import sys

antKommandoer = int(sys.stdin.readline())
for _ in range(antKommandoer):
    kommando = sys.stdin.readline().split()
    if len(kommando) <= 2:
        print()
    elif kommando[0] == "simon" and kommando[1] == "says":
        print(*kommando[2:])
    else:
        print()