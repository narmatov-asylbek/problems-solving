
def find_max(node) -> int:
    res = float('-inf')

    def depth(node):
        nonlocal res
        if not node:
            return
        
        left_min, left_max = depth(node.left) or (node.val, node.val)
        right_min, right_max = depth(node.right) or (node.val, node.val)

        all_min = min(left_min, right_min)
        all_max = max(left_max, right_max)

        diff = max(abs(node.val - all_min), abs(node.val - all_max))
        res = max(diff, res)
        curr_min = min(all_min, node.val)
        curr_max = max(all_max, node.val)
        return (curr_min, curr_max)
    depth(node)
    return res