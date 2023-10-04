# Heaps
import heapq

# to find the min and max for a certain 
# values frequently, under the hood are
# arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)

# by default heaps in python are min heap

# min is always at index 0
print(minHeap[0])

# popping values from a heap
while len(minHeap):
    print(heapq.heappop(minHeap))