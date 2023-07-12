import sys
n = int(input())
NGE = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and NGE[stack[-1]] < NGE[i]:
        answer[stack.pop()] = NGE[i]
    stack.append(i)


print(*answer)