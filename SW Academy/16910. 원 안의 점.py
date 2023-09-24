t = int(input())
for test_case in range(t):
    n = int(input())
    points = (n - 1) * 4 + 5
    cnt = 0

    for i in range(1, n):
        for j in range(1, n):
            if (i**2) + (j**2) <= n**2:
                cnt += 1

    points += (cnt * 4)
    print(f"#{test_case+1} {points}")

