from collections import deque  

q = deque()
q = deque(maxlen = 4) # when q is full still enqueue, the left one will be deleted
print(q)
q.append(1)
q.popleft()
q.clear()
print(len(q))