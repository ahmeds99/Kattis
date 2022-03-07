import sys
import bisect
from collections import Counter

"""
IKKE GODKJENT ALLE TESTER
"""

# kommandoer = {"en": en}
info = sys.stdin.readline().split()
antTall = int(info[0])
kommando = int(info[1])
liste = sys.stdin.readline().split()

if kommando == 1:
    funnet = False
    unike = set(liste)
    for i in range(1, 7777):
        if not funnet and str(i) in unike and str(7777 - i) in unike:
            print("Yes")
            funnet = True
            break
    
    if not funnet:
        print("No")

elif kommando == 2:
    unike = set(liste)
    
    if len(unike) == antTall:
        print("Unique")
    else:
        print("Contains duplicate")

elif kommando == 3:
    flest, forekomster = Counter(liste).most_common(1)[0]
    if forekomster > antTall / 2:
        print(flest)
    else:
        print(-1)

elif kommando == 4:
    liste = sorted(liste)
    if antTall % 2 == 1:
        print(liste[antTall // 2])
    else:
        print(*liste[antTall // 2 - 1 : antTall // 2 + 1])

elif kommando == 5:
    sortert = sorted(filter(lambda tall: 99 < int(tall) < 1000, liste))
    print(*sortert)
    # for tall in liste:
    #     tall = int(tall)
    #     if 100 <= tall <= 999:
    #         bisect.insort(sortert, tall)
    
    # for t in sortert:
    #     print(t, end=" ")