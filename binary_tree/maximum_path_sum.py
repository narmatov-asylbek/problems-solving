


def maximum_path_sum(node) -> int:
    res = float('-inf')

    def depth(node):
        nonlocal res
        if not node:
            return 0
        left_sum = max(depth(node.left), 0)
        right_sum = max(depth(node.right), )

        curr_sum = left_sum + right_sum + node.val
        res = max(curr_sum, res)
        return node.val + max(left_sum, right_sum)
    depth(node)
    return res