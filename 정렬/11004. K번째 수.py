n, k = map(int, input().split())
A = list(map(int, input().split()))

# A.sort()
# print(A[k-1])

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = []; right = []; equal = []
    for i in array:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)

answer = quick_sort(A)
print(answer[k-1])

