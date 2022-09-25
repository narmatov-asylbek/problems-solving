


def max_product(nums: list[int]) -> int:
    curr = max(nums)

    cur_min, cur_max = 1, 1

    for n in nums:
        if n == 0:
            cur_min = cur_max = 1
            continue
        temp = cur_max * n
        cur_max = max(n * cur_max, n * cur_min, n)
        cur_min = min(temp, n * cur_min, n)
        res = max(cur_max, cur_min, res)
    
    return res

print(max_product([2, 3, -2, 4]))
print(max_product([-2, 0, -1]))