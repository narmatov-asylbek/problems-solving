

def jump(nums: list[int]) -> int:
    res = 0
    left = right = 0

    while right < len(nums) - 1:
        k = 0

        for i in range(left, right + 1):
            k = max(k, i + nums[i])
        
        left = right + 1
        right = k
        res += 1
    return res