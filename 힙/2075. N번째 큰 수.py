import sys
import heapq

n = int(input())
h = []
for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        if len(h) <= n:
            heapq.heappush(h, (-nums[i], nums[i]))
        else:
            heapq.heappop(h)

    print(h[-1][1])