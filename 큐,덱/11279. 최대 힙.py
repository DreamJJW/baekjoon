import heapq
import sys

n = int(input())
h = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a > 0:
        heapq.heappush(h, (-a, a))
    else:
        if h:
            print(heapq.heappop(h)[-1])
        else:
            print(0)