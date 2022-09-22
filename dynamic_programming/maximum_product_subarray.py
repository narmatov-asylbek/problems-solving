


def max_product(nums: list[int]) -> int:
    curr = nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] * dp[i - 1])
        curr = max(dp[i], curr)
    return curr

print(max_product([2, 3, -2, 4]))
print(max_product([-2, 0, -1]))