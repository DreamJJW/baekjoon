from collections import deque

T = int(input())
for i in range(T):
    p = input()
    n = int(input())
    lst = input()[1:-1].split(',')

    queue = deque()

    for j in lst:
        queue.append(j)

    cnt = 0

    if n == 0:
        print('error')
        break

    for order in p:
        if order == 'R':
            cnt += 1
        elif order == 'D':
            if cnt % 2 != 0:
                queue.reverse()
                cnt = 0
            if queue:
                queue.popleft()
            else:
                print('error')
                break

    if queue:
        answer = []
        for k in queue:
            answer.append(k)

    print(answer)

