from QueueImplementation_v1 import QueueImplementation

input = [1,2,3,4,5,6,7,8,9,10,2,5]

q = QueueImplementation()

for x in input:
    q.enqueue(x)


q.print_all()