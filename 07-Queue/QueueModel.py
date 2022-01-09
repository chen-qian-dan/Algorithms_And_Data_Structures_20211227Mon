import queue as q
myQ = q.Queue(maxsize = 3)
print(myQ.qsize())

print(myQ.empty())
myQ.put(1)
myQ.put(2)
myQ.put(3)
print(myQ.full())
print(myQ.qsize())
print(myQ.get())
print(myQ.qsize())