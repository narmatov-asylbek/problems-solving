
def helper(nums: list[int]) -> int:
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]

    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
    return dp[-1]

def house_robber(nums: list[int]):
    if len(nums) < 2:
        return nums[0]
    return max(helper(nums[1:]), helper(nums[:len(nums)-1]))
