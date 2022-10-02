def helper(nums: list[int], current: list[int], res: list[int], target: int) -> list[int]:
    if target < 0:
        return
    if target == 0:
        res.append(current)
        return
    for num in nums:
        l = list(current)
        l.append(num)
        helper(nums, l, res, target - num)


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    s = []
    helper(candidates, [], s, target)
    return s


print(combination_sum([2,3,6,7], 7))
print(combination_sum([2, 3, 5], 8))
print(combination_sum([2], 8))