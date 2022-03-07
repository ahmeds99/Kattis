import sys, heapq

antallCaser = int(sys.stdin.readline())

for i in range(antallCaser):
    salgsHeap = []
    kjøpsHeap = []
    sisteTransaksjon = 0
    antallOrdre = int(sys.stdin.readline())

    for j in range(antallOrdre):
        info = sys.stdin.readline().split()
        type = info[0]
        antall = int(info[1])
        pris = int(info[-1])

        if type == "buy":
            heapq.heappush(kjøpsHeap, (-pris, antall))
        else: 
            heapq.heappush(salgsHeap, (pris, antall))

        while salgsHeap and kjøpsHeap and -kjøpsHeap[0][0] >= salgsHeap[0][0]:
            sisteTransaksjon = salgsHeap[0][0]
            
            if kjøpsHeap[0][1] == salgsHeap[0][1]:
                heapq.heappop(kjøpsHeap)
                heapq.heappop(salgsHeap)

            elif kjøpsHeap[0][1] > salgsHeap[0][1]:
                kjøpsHeap[0] = (kjøpsHeap[0][0], kjøpsHeap[0][1] - salgsHeap[0][1])
                heapq.heappop(salgsHeap)
            
            else:
                salgsHeap[0] = (salgsHeap[0][0], salgsHeap[0][1] - kjøpsHeap[0][1])
                heapq.heappop(kjøpsHeap)
        
        if salgsHeap and kjøpsHeap and -kjøpsHeap[0][0] >= salgsHeap[0][0]:
            sisteTransaksjon = salgsHeap[0][0]
            
            if kjøpsHeap[0][1] == salgsHeap[0][1]:
                heapq.heappop(kjøpsHeap)
                heapq.heappop(salgsHeap)

            elif kjøpsHeap[0][1] > salgsHeap[0][1]:
                kjøpsHeap[0] = (-kjøpsHeap[0][0], kjøpsHeap[0][1] - salgsHeap[0][1])
                heapq.heappop(salgsHeap)
            
            else:
                salgsHeap[0] = (salgsHeap[0][0], salgsHeap[0][1] - kjøpsHeap[0][1])
                heapq.heappop(kjøpsHeap)

        printStreng = ""
        if salgsHeap:
            printStreng += str(salgsHeap[0][0]) + " "
        else:
            printStreng += "- "

        if kjøpsHeap:
            printStreng += str(-kjøpsHeap[0][0]) + " "
        else:
            printStreng += "- "

        if sisteTransaksjon == 0:
            printStreng += "-"
        else:
            printStreng += str(sisteTransaksjon)

        print(printStreng)