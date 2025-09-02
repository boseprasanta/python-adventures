from collections import deque

queue = deque()

queue.append(1)
queue.append(2)

print(queue)  # deque([1, 2])

queue.appendleft(-1)

print(queue)  # deque([-1, 1, 2])

y = queue.pop()

print(y)  # 2
print(queue)  # deque([-1, 1])