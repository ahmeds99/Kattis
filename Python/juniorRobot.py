import sys

antTall = int(sys.stdin.readline())
tidligereStorste = None
antallDager = 0

tallene = sys.stdin.readline().strip().split()
barGain = 0

for i in range(len(tallene)):
    j = i - 1
    nåværendeBeste = -1
    while j >= 0 and tallene[j] > tallene[i]:
        j -= 1
        nåværendeBeste = i - j
    # for j in range(i - 1, -1, -1):
    #     if (int(tallene[i]) < int(tallene[j])):
    #         nåværendeBeste = i - j
    #     else:
    #         break
    if nåværendeBeste > barGain:
        barGain = nåværendeBeste
        
if (barGain == 0):
    print("infinity")
else:
    print(barGain)

