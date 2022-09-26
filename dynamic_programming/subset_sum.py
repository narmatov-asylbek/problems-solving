

def subset_sum(nums: list[int], s: int) -> bool:
    n = len(nums)
    dp = [[False for _ in range(s + 1)] for _ in range(n)]

    for i in range(0, n):
        dp[i][0] = True
    
    for i in range(1, s + 1):
        dp[0][i] = True if nums[0] == i else False
    
    for i in range(1, n):
        for j in range(1, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]
    return dp[n - 1][s]
