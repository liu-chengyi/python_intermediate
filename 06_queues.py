import queue

q = queue.Queue() # first in first out
slack = queue.LifoQueue() # last in first out
q_priority = queue.PriorityQueue()


numbers = [10, 20, 30, 40, 50, 60, 70]

for number in numbers:
    q.put(number)

# q.get() always returns the first element in the queue
print(q.get())

# add (priority, value) as tuple - the lower the higher priority
q_priority.put((2, "Hello World!"))
q_priority.put((11, 99))
q_priority.put((5, 7.5))
q_priority.put((1, True))

while not q_priority.empty():
    # print only the value
    print(q_priority.get()[1])

