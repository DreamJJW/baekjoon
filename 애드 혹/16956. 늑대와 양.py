r, c = map(int, input().split())
board = []
answer = 1
for _ in range(r):
    board.append(list(input()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(r):
    for j in range(c):
        if board[i][j] == '.':
            board[i][j] = 'D'

for i in range(r):
    for j in range(c):
        if board[i][j] == 'W':
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]

                if x < 0 or x > r or y < 0 or y > c:
                    continue

                if board[x][y] == 'S':
                    answer = 0
                    break

print(answer)