import heapq
import sys

n = int(input())
h = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a > 0:
        heapq.heappush(h, a)
    else:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)

