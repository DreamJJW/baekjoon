x, y = map(int, input().split())
z = (y * 100) // x
def binary_search(start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if z >= 99:
            return -1
        if ((mid + y) // (mid + x) * 100) > z:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

res = binary_search(x, y)
print(res)