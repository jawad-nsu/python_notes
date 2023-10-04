# Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1) # adds item to the right of the queue
queue.append(2) 
print(queue)

# the benefit of using a queue is we can pop item from left 
# in constant time which is not possible with a stack
queue.popleft()
print(queue)

# since this is double ended, we can add values 
# to the end of the queue as well
queue.appendleft(1)
print(queue)