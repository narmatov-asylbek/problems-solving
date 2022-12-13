


def range_sum(root, low: int, high: int) -> int:
    res = 0
    
    def depth(node):
        nonlocal res
        if not node:
            return
        if low <= node.val <= high:
            res += node.val
        if node.val <= high:
            depth(node.right)
        if node.val >= low:
            depth(node.left)
    
    depth(root)
    return res
