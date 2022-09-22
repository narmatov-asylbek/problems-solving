

def house_robber(nums: list[int]) -> int:
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]

    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
    return dp[-1]

print(house_robber([1, 2, 3, 1]))
print(house_robber([2, 7, 9, 3, 1])) 