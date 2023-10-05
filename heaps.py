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


# No max heaps by default, work around is
# to use min heap and multiply by -1 when
# push & pop.
maxHeap = [] 
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
# negative numbers get smaller and smaller
# the farther they are from zero
# that's why -4 is smaller than -3
# and since -4 is the smallest, it'll be
# at index 0. 

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# If you already have the values to create a heap
# we can create the heap in linear time 
# Build heap from initial values
arr = [1, 2, 3, 4, 5]
heapq.heapify(arr)
while len(arr):
    print(heapq.heappop(arr))