import queue as q 

myQ = q.Queue(maxsize= 3)
print(myQ.qsize())
myQ.put(1) # enqueue
myQ.put(2)
myQ.put(3)

print(myQ.qsize())
print(myQ.get()) # dequeue