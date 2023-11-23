from collections import deque
graph = [[], [2,3,6]]
queue = deque()
queue.append(1)
queue.extend(graph[1])

print(queue)