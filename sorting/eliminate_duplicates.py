

def eliminate(nums: list[int]) -> int:
    write_idx = 1

    for num in nums[1:]:
        if nums[write_idx - 1] != num:
            nums[write_idx] = num
            write_idx += 1
    return write_idx