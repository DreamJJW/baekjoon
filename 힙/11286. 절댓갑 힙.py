import sys
import heapq

n = int(input())
h = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(h, (abs(num), num))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)

