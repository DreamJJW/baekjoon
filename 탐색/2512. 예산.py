import sys

def binary_search(array, start, end):
    answer = 0
    while start <= end:
        money = 0
        mid = (start + end) // 2
        for i in array:
            if i > mid:
                money += mid
            else:
                money += i

        if money <= budget:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer

n = int(input())
requests = list(map(int, sys.stdin.readline().split()))
budget = int(input())
requests.sort()

res = binary_search(requests, 1, requests[-1])
print(res)