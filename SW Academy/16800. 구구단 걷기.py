import math
t = int(input())
for test_case in range(t):
    n = int(input())

    dis = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            dis.append(i)

    answer = (dis[-1] - 1) + (n // dis[-1]) - 1
    print(f"#{test_case+1} {answer}")