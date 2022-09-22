def recurse(nums, left, right, target):
    if left > right:
        return - 1

    middle = left + (right - left) // 2

    if nums[middle] == target:
        return middle
    elif nums[middle] > target:
        right = middle - 1
    else:
        left = middle + 1
    return recurse(nums, left, right, target)


def search(nums, target) -> int:
    ...

print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,0,1,2], 3))
print(search([1], 0))
print(search([3, 1], 4))
print(search([3, 1], 1))

