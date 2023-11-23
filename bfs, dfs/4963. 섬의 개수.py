import sys
sys.setrecursionlimit(10 ** 6)

dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]


def dfs(x, y):
    visited.append((x, y))
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 밖이면 continue
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue

        # 바다라면 continue
        if board[nx][ny] == 0:
            continue

        # 땅이라면 진행
        if board[nx][ny] == 1 and (nx, ny) not in visited:
            dfs(nx, ny)


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == h == 0:
        break
    board = []
    for _ in range(h):
        board.append(list(map(int, sys.stdin.readline().split())))

    answer = 0
    visited = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and (i, j) not in visited:
                dfs(i, j)
                answer += 1

    print(answer)
