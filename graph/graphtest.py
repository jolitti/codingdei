from queue import PriorityQueue

q = PriorityQueue()

q.put((1,2))
q.put((2,-1))
print(q.get())
print(q.get())