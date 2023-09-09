t = int(input())
for test_case in range(t):
    x = []
    n, m = map(int, input().split())
    for i in range(n):
        x.append(list(map(int, input().split())))

    answer = []
    for row in range(n-m+1):
        for col in range(n-m+1):
            temp = 0
            for a in range(m):
                for b in range(m):
                    temp += x[a + row][b + col]
            answer.append(temp)

    print(f"#{test_case+1} {max(answer)}")