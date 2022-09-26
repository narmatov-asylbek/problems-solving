# Solution is actually a dynamic programming

def jump_game(nums: list[int]) -> bool:
    dp = [False for _ in range(len(nums))]

    for index, step in enumerate(nums):
        dp[index: index + step] = True
    
    return all(dp)


print(jump_game([2,3,1,1,4]))
print(jump_game([3,2,1,0,4]))