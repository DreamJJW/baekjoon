import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

t = int(input())
for i in range(t):
    n = int(input())
    note_one = list(map(int, input().split()))
    m = int(input())
    note_two = list(map(int, input().split()))

    note_one.sort()

    for i in note_two:
        if binary_search(note_one, i, 0, n - 1):
            print(1)
        else:
            print(0)