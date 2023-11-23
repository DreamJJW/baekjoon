from collections import deque

def dfs(start_node):
    global cnt
    visited[start_node] = 1
    for i in graph[start_node]:
        if visited[i] != 1:
            cnt += 1
            dfs(i)

    print(visited)
    return cnt

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(1))
