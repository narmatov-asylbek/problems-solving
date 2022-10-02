def jump_game_dp(nums: list[int]) -> bool:
    n = len(nums)
    if n == 1:
        return True
    
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(1, n - 1):
        if dp[i - 1] < i:
            return False
        
        dp[i] = max(i + nums[i], dp[i - 1])

        if dp[i] >= n - 1:
            return True
    return dp[len(nums) - 2] >= n - 1


def jump_game_greedy(nums: list[int]) -> bool:
    goal = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0


print(jump_game_dp([2,3,3,0,4]))
print(jump_game_dp([0,3,1,1,4]))
print(jump_game_dp([3,2,1,0,4]))