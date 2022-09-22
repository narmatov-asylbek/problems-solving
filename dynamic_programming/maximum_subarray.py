

def max_sub_array(nums: list[int]) -> int:
    curr = nums[0]

    for i in range(1, len(nums)):
        nums[i] = max(nums[i - 1] + nums[i], nums[i])
        curr = max(nums[i], curr)
    return curr


print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
print(max_sub_array([5,4,-1,7,8]))
print(max_sub_array([1]))