import random
queue = []
numberOfNumbers = 10
rangeTo = 100
for i in range(numberOfNumbers):
    queue.append(random.randint(0, rangeTo))
print(f"queue is {queue}")

while len(queue) > 0:
    currentNumber = queue.pop(0)
    print(f"currentNumber is {currentNumber}, queue is {queue}")
print ("the queue is now empty") # type: ignore