

# O(n ^ 2) time, O(n) space
def lis(nums: list[int]) -> int:
    dp = [1 for _ in range(len(nums))]

    for i, val in enumerate(nums):
        if i == 0:
            continue

        cur_lis = 0
        for j in range(i):
            if nums[j] < val:
                cur_lis = max(cur_lis, dp[j])
        dp[i] = cur_lis + 1
    
    return max(dp)


print(lis([10,9,2,5,3,7,101,18]))
print(lis([0,1,0,3,2,3]))
print(lis([7,7,7,7,7,7,7]))