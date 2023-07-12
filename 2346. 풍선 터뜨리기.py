import sys
from collections import deque
N = int(input())
order = list(map(int, sys.stdin.readline().split()))
answer = []

d = deque()

for i, j in enumerate(order):
    d.append((i, j))

while d:
    a, b = d.popleft()
    answer.append(a + 1)
    if b > 0:
        d.rotate(-b + 1)
    else:
        d.rotate(-b)


print(*answer)











