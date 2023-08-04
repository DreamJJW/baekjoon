def binary_search(array, start, end):
    answer = 0
    while start <= end:
        cut = 0
        mid = (start + end) // 2
        for a in array:
            cut += a // mid
        if cut < n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid
    return answer


k, n = map(int, input().split())
line = []
for i in range(k):
    num = int(input())
    line.append(num)

line.sort()
res = binary_search(line, 0, line[-1])
print(res)
