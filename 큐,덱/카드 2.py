from collections import deque
N = int(input())
d = deque()

for i in range(1, N + 1):
    d.append(i)

while len(d) > 1:
    d.popleft()
    a = d.popleft()
    d.append(a)

print(d[0])