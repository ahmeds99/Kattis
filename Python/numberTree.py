import sys 

info = sys.stdin.readline().split()
høyde = int(info[0])
rot = 2 ** (høyde + 1) - 1

if (len(info) == 1):
    print(rot)
else:
    nåværendeTall = rot
    nåværendeHøyde = 1
    for kommando in info[1]:
        distanseFraRot = rot - nåværendeTall
        if kommando == "L":
            nåværendeTall -= (distanseFraRot + 1)
        else:
            nåværendeTall -= (distanseFraRot + 2)
            
        nåværendeHøyde += 1

    print(nåværendeTall)