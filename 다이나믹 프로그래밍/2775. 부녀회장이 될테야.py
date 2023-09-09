t = int(input())

for test_case in range(t):
    k = int(input())
    n = int(input())
    apart = [[0 for col in range(14)] for row in range(k+1)]

    for a in range(0, 14):
        apart[0][a] = a + 1

    for b in range(0, k+1):
        apart[b][0] = 1

    for i in range(1, k+1):
        for j in range(1, 14):
            apart[i][j] = apart[i-1][j] + apart[i][j-1]

    print(apart[k][n-1])
