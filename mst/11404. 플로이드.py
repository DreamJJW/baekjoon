INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 노드의 개수 만큼 간선 그래프 선언

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a][b] = min(graph[a][b], c)

for g in range(1, n + 1):
    for h in range(1, n + 1):
        for j in range(1, n + 1):
            graph[h][j] = min(graph[h][j], graph[h][g] + graph[g][j])


for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == 1e9:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

