import heapq
import sys
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


v, e = map(int, sys.stdin.readline().split())  # v 노드, e 간선
k = int(input())  # start
INF = int(1e9)
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
for _ in range(e):
    u, V, w = map(int, sys.stdin.readline().split())
    graph[u].append((V, w))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

