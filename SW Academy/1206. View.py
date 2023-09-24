t = 10
for test_case in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    answer = 0
    for i in range(2, len(b) - 2):
        if b[i] > b[i+1] and b[i] > b[i+2] and b[i] > b[i-1] and b[i] > b[i-2]:
            answer += min(b[i] - b[i+1], b[i] - b[i+2], b[i] - b[i-1], b[i] - b[i-2])

    print(f"#{test_case+1} {answer}")