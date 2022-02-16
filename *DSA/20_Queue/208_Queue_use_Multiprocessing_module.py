from multiprocessing import Queue 

q = Queue(maxsize = 3)
q.put(1) # enqueue
q.get() # dequeue 
