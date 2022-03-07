import sys

"""
IKKE FERDIG
"""

def antallForhold(tall):
    if tall < 2:
        return 0   
    if tall == 2:
        return 1
    else:
        return tall + antallForhold(tall - 1)

print(antallForhold(int(sys.stdin.readline())))