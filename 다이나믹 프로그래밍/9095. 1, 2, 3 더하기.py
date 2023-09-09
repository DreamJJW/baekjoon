t = int(input())

for test_case in range(t):
    n = int(input())
    temp = [0] * 11
    answer = 0

    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    elif n == 3:
        answer = 4
    else:
        temp[0] = 1
        temp[1] = 2
        temp[2] = 4

        for i in range(3, n):
            temp[i] = temp[i-1] + temp[i-2] + temp[i-3]

        answer = temp[n-1]
    print(answer)
