t = int(input())
for test_case in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    cnt = 0
    for i in range(1, n-1):
        if p[i] != max(p[i-1], p[i], p[i+1]) and p[i] != min(p[i-1], p[i], p[i+1]):
            cnt += 1

    print(f"#{test_case+1} {cnt}")
