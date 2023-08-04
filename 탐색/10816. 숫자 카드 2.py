from bisect import bisect_left, bisect_right

def count_by_range(b, left_value, right_value):
    right_index = bisect_right(b, right_value)
    left_index = bisect_left(b, left_value)
    return right_index - left_index

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
target_nums = list(map(int, input().split()))
cards.sort()

answer = []

for i in target_nums:
    answer.append(count_by_range(cards, i, i))

print(*answer)