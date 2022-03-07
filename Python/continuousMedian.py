import bisect
import sys

"""
Tregere løsning, består nesten alle testcaser men failer på de siste. Prøver meg i Java istedenfor, 
ved å bruke to heaps, en for nedre og en for øvre halvdel, der nedre er en max-heap og den øvre er en min-heap. 
"""
antallCaser = int(sys.stdin.readline())

for i in range(antallCaser):
    lengde = int(sys.stdin.readline())
    sortert = []
    totalMedian = 0
    alleTall = sys.stdin.readline().split()

    for tall in alleTall:
        bisect.insort(sortert, int(tall))
        if len(sortert) % 2 == 0:
            venstreMid = int(len(sortert) / 2) - 1
            høyreMid = int(len(sortert) / 2)
            median = int((sortert[venstreMid] + sortert[høyreMid]) / 2)
        else:
            median = sortert[int(len(sortert) / 2)]
        
        totalMedian += median 
    
    print(totalMedian)
