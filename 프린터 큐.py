a = int(input())
for i in range(a):
    N, M = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    cnt = 0
    x = queue[M]
    while True:
        if x not in queue:
            break
        if queue[0] == max(queue):
            del queue[0]
            cnt += 1
        else:
            queue.append(queue[0])
            del queue[0]
    print(cnt)







