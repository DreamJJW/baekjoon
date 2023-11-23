t = int(input())
for test_case in range(t):
    n = int(input())
    board = []

    for i in range(n):
        board.append(list(map(str, input())))

    answer = "NO"
    
    # 가로 판별
    row_cnt = 0
    for i in board:
        for j in i:
            if j == 'o':
                row_cnt += 1
            else:
                row_cnt = 0
            if row_cnt >= 5:
                answer = "YES"
                break

    # 세로 판별
    col_cnt = 0
    for i in range(n):
        for j in range(n):
            if board[j][i] == 'o':
                col_cnt += 1
            else:
                col_cnt = 0
            if col_cnt >= 5:
                answer = "YES"
                break

    # 대각 판별
    diag_cnt = 0
    for i in range(n):
        if board[i][i] == 'o':
            diag_cnt += 1
        else:
            diag_cnt = 0
        if diag_cnt == 5:
            answer = "YES"
            break

    reversed_diag_cnt = 0
    for i in range(n):
        if board[i][n-i-1] == 'o':
            reversed_diag_cnt += 1
        else:
            reversed_diag_cnt = 0
        if reversed_diag_cnt == 5:
            answer = "YES"
            break

    # 윗 대각


    # 아랫 대각

    print(f"#{test_case+1} {answer}")
    
    
