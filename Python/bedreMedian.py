import bisect
import heapq
import sys

antallCaser = int(sys.stdin.readline())

for i in range(antallCaser):
    lengde = int(sys.stdin.readline())
    minHeap = []
    maxHeap = []
    totalMedian = 0
    alleTall = sys.stdin.readline().split()

    for tall in alleTall:
        tall = int(tall)
        
        if not maxHeap and not minHeap:
            heapq.heappush(minHeap, tall)
        elif not maxHeap:
            if tall > minHeap[0]:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
                heapq.heappush(minHeap, tall)
            else:
                heapq.heappush(maxHeap, -tall)
        
        elif len(minHeap) == len(maxHeap):
            if tall < -maxHeap[0]:
                heapq.heappush(maxHeap, -tall)
            else:
                heapq.heappush(minHeap, tall)

        elif len(maxHeap) > len(minHeap):
            if tall < -maxHeap[0]:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
                heapq.heappush(maxHeap, -tall)
            else:
                heapq.heappush(minHeap, tall)
        
        else:
            if tall > minHeap[0]:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
                heapq.heappush(minHeap, tall)
            else:
                heapq.heappush(maxHeap, -tall)

        if len(minHeap) == len(maxHeap):
            median = int(int(minHeap[0] + -maxHeap[0]) / 2)
        elif len(minHeap) > len(maxHeap):
            median = minHeap[0]
        else:
            median = -maxHeap[0]
        totalMedian += median
   
    print(totalMedian)
