import sys
sys.setrecursionlimit(10**6)
def dfs(start, graph):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(node, graph)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
visited = []
for i in range(1, n+1):
    if i not in visited:
        dfs(i, graph)
        answer += 1

print(answer)