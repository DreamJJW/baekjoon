from collections import deque

N, M = map(int, input().split())
order = list(map(int, input().split()))

cnt = 0
queue = deque()
for i in range(1, N+1):
    queue.append(i)

while order:

    a = len(queue) // 2

    if queue[0] == order[0]:
        queue.popleft()
        order.pop(0)
    else:
        if queue.index(order[0]) <= a:
            queue.append(queue[0])
            queue.popleft()
            cnt += 1
        else:
            queue.appendleft(queue[-1])
            queue.pop()
            cnt += 1

print(cnt)

