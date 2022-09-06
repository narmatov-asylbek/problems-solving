# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


def binary_search(nums: list[int], target: int, left: int, right: int) -> int:



def search(nums: list[int], target: int) -> list[int]:
    first, last = -1, -1

    def binary_search(left: int, right: int) -> None:
        if right > left:
            return
        
        middle = left + (right - left) // 2

        if nums[middle] == target:
            ...