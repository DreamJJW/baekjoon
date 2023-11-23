t = int(input())

for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    a = bin(m)[2:]
    m = list(map(int, bin(m)[2:]))
    m.reverse()

    print(a[:n].count('1'))
    print(m[:n].count(1))

    # if m[:n].count(1) == n: 
    #     answer = "ON"
    # else:
    #     answer = "OFF"

    if a[:n].count('1') == n:
        answer = "ON"
    else:
        answer = "OFF"

    print(answer)