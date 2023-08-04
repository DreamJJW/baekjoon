import sys

def binary_search(array, start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        cut = 0
        for i in array:
            if i > mid:
                cut += i - mid
        if cut > m:
            start = mid + 1
            answer = mid

        elif cut == m:
            return mid
        else:
            end = mid - 1
    return answer


n, m = map(int, input().split())
tree = list(map(int, sys.stdin.readline().split()))

tree.sort()
max_tree_height = tree[-1]

a = binary_search(tree, 0, max_tree_height)
print(a)
