n = int(input())
graph = []
for i in range(n):
    edges = list(map(int, input().split()))
    graph.append(edges)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for i in graph:
    for j in i:
        print(j, end=" ")
    print()
