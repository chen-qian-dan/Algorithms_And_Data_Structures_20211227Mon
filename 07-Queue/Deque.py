# How to use collections.deque as a FIFO queue:
from collections import deque

q = deque(maxlen = 3)
print(q)

q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
print(q.clear())
print(q)
