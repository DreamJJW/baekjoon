from collections import deque

n, w, L = list(map(int, input().split()))
trucks = list(map(int, input().split()))

deq = deque()

for i in trucks:
    deq.append(i)

answer = 0
bridge = deque([0] * w)

while bridge:
    answer += 1
    if bridge:
        bridge.popleft()
    if deq:
        if sum(bridge) + deq[0] <= L:
            bridge.append(deq.popleft())
        else:
            bridge.append(0)

print(answer)








