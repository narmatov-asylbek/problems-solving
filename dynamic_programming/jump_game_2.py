


def jump(nums: list[int]) -> int:
    n = len(nums)

    if n == 1:
        return 0

    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            if i <= j + nums[j]:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]



print(jump([2,3,1,1,4]))
print(jump([2,3,0,1,4]))