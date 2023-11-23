from collections import Counter
import sys

n = int(input())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
temp = []

print(round(sum(nums) / n))
print(nums[n // 2])

cnt = 0
max_num = Counter(nums).most_common()[0][1]
for i in Counter(nums).most_common():
    if i[1] == max_num:
        cnt += 1

if cnt > 1:
    print(Counter(nums).most_common()[1][0])
else:
    print(Counter(nums).most_common()[0][0])

print(nums[-1] - nums[0])
