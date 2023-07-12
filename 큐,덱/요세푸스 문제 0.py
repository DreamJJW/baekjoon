from collections import deque
N, K = map(int, input().split())
d = deque()
temp = []
for i in range(1, N + 1):
    d.append(i)

cnt = 1

while True:
    if len(temp) == N:
        break

    if cnt % K == 0:
        temp.append(d[0])
        d.popleft()
    else:
        d.append(d[0])
        d.popleft()

    cnt += 1

print("<",end='')
for i in range(len(temp)-1):
    print("%d, "%temp[i], end='')
print(temp[-1], end='')
print(">")