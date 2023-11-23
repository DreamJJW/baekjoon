from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    need_visited = deque()
    need_visited.append((x, y))  # 시작 좌표 삽입
    visited[x][y] = 1  # 좌표 방문 처리
    cnt = 1

    while need_visited:
        x, y = need_visited.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            # 상하좌우 탐색이 범위를 넘지 않으며, 방문하지 않았고(visited = 0), 그래프에서의 좌표가 집(1)이라면
            if (0 <= nx < n) and (0 <= ny < m) and visited[nx][ny] == 0 and land[nx][ny] == 1:
                need_visited.append((nx, ny))
                visited[nx][ny] = 1  # 방문처리
                cnt += 1  # 단지의 수 카운트
    return cnt

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    land = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        land[x][y] = 1

    answer = []
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                answer.append(dfs(i, j))


    print(len(answer))
