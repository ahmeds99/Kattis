import sys

antStatuer = int(sys.stdin.readline())
antallDager = 0
printere = 1
antPrintet = 0

while (antPrintet < antStatuer):
    if antStatuer - antPrintet > printere:
        printere += printere
        antallDager += 1
    else:
        antallDager += 1
        antPrintet += printere

print(antallDager)