t = int(input())
for test_case in range(t):
    nums = sorted(list(map(int, input().split())))
    print(f"#{test_case+1} {round(sum(nums[1:-1]) / 8)}")
    