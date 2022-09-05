

def helper(node, current):
    if not node:
        return 0
    if not node.left and not node.right:
        return int(current + str(node.val), base=2)
    return helper(node.left, current + str(node.val)) + helper(node.right + str(node.val))
    


def binary_sum_to_leaf(root):
    return helper(root, "")