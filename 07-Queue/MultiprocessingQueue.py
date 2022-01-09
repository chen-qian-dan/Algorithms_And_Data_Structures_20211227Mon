# How to use multiprocessing.Queue as a FIFO queue

from multiprocessing import Queue 

myq = Queue(maxsize = 3)
myq.put(1)
print(myq.get())
