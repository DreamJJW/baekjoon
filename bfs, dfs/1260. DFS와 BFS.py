from collections import deque
def dfs(start, g):
    if start in visited1:
        return

    visited1.append(start)
    print(start, end=' ')

    for node in g[start]:
        dfs(node, g)


def bfs(start, g):
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node not in visited2:
            print(node, end=' ')
            visited2.append(node)
            queue.extend(g[node])


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited1 = []
visited2 = []
dfs(v, graph)
print()
bfs(v, graph)
