# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


from typing import Callable


def find(nums: list[int], target: int, op: Callable[[int, int, int], tuple[int]]) -> int:
    position = -1

    left, right = 0, len(nums) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if nums[middle] == target:
            position = middle
            left, right = op(left, right, middle)
        elif nums[middle] < target:
            left += 1
        else:
            right -= 1
    return position


def search(nums: list[int], target: int) -> list[int]:
    first = find(nums, target, lambda x, _, z: (x, z - 1))
    last = find(nums, target, lambda _, y, z: (z + 1, y))

    return ([first, last] if last >= first else [-1, -1])

print(search([5, 7, 7, 8, 8, 10], 8))
print(search([5, 7, 7, 8, 8, 10], 6))
print(search([], 0))