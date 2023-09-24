t = int(input())
for test_case in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    dp = [0] * n
    temp = []

    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
    temp.append(max(dp))

    print(f"#{test_case + 1} {max(temp)}")