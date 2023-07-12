from collections import deque
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    queue = deque()

    for a in weight:
        queue.append(a)

    cnt = 1
    idx = M  # 출력하려는 문서의 index

    while queue:
        if queue[0] == max(queue):
            if idx == 0:
                print(cnt)
                break
            queue.popleft()
            cnt += 1
            idx -= 1

        else:
            queue.append(queue[0])
            queue.popleft()
            if idx == 0:
                idx = len(queue) - 1
            else:
                idx -= 1








