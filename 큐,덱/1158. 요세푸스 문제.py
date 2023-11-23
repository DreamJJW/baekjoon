from collections import deque

n, k = map(int, input().split())
q = deque()
for i in range(1, n+1):
    q.append(i)

cnt = 0
temp = []

while q:
    a = q.popleft()
    cnt += 1

    if cnt == k:
        temp.append(a)
        cnt = 0
    else:
        q.append(a)

print("<", end='')
for i in range(len(temp) - 1):
    print(str(temp[i])+', ', end='')
print(temp[-1], end='')
print(">")
