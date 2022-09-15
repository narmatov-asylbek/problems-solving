class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_max(nums: list[int]) -> tuple[int, int]:
    max_val = float('-inf')
    max_index = 0

    for i, v in enumerate(nums):
        if v > max_val:
            max_val = v
            max_index = i
    return max_index, max_val

def max_tree(nums: list[int]) -> TreeNode | None:
    if not nums:
        return
    if len(nums) == 1:
        return TreeNode(nums[0])
    max_index, max_val = find_max(nums)
    node = TreeNode(max_val)
    node.left = max_tree(nums[:max_index])
    node.right = max_tree(nums[max_index + 1:])
    return node