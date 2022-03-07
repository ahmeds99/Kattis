# IKKE FERDIG

import sys

førsteInfo = sys.stdin.readline().split()
antallFilmer = int(førsteInfo[0])
filmerPåHorrorListe = int(førsteInfo[1])
antallLikheter = int(førsteInfo[2])

andreInfo = sys.stdin.readline().split()
horrorListe = [int(x) for x in andreInfo]

for i in range(antallLikheter):
    info = sys.stdin.readline().split()
    filmA = int(info[0])
    filmB = int(info[1])

