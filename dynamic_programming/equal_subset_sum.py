def can_partition(nums: list[int]) -> bool:
    s = sum(nums)

    if s % 2 != 0:
        return False

    s = int(s / 2)

    n = len(nums)

    dp = [[False for _ in range(s + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    
    for j in range(1, s + 1):
        dp[0][j] = nums[0] == j
    
    for i in range(1, n):
        for j in range(1, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]
    return dp[n - 1][s]
    