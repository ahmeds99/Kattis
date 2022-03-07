import sys

oppgavene = sys.stdin.readline().split(";")
total = 0

for oppgave in oppgavene:
    if "-" in oppgave:
        delBindestrek = oppgave.split("-")
        lengdeDel = int(delBindestrek[1]) - int(delBindestrek[0]) + 1
        total += lengdeDel
    else:
        total += 1

print(total)