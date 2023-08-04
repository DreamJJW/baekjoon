import sys
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False

n = int(input())
cards = list(map(int, sys.stdin.readline().split()))
m = int(input())
target_nums = list(map(int, sys.stdin.readline().split()))

cards.sort()

for i in target_nums:
    if binary_search(cards, i, 0, n - 1):
        print(1, end=' ')
    else:
        print(0, end=' ')