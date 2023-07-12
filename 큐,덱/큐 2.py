from collections import deque
import sys

a = deque()
N = int(input())
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        a.append(order[1])
    elif order[0] == 'front':
        if a:
            print(a[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if a:
            print(a[-1])
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(a))
    elif order[0] == 'pop':
        if a:
            print(a[0])
            a.pop()
        else:
            print(-1)
    elif order[0] == 'empty':
        if a:
            print(0)
        else:
            print(1)