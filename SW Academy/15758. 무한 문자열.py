t = int(input())
for test_case in range(t):
    S, T = map(str, input().split())
    answer = "no"
    if S == T:
        answer = "yes"

    if len(S) * T == len(T) * S:
        answer = "yes"

    print(f"#{test_case+1} {answer}")

