

def validate_bst(node, left, right) -> bool:
    if not node:
        return True
    if node.val > left or node.val < right:
        return False
    return validate_bst(node.left, node.val, right) and validate_bst(node.right, left, node.val)


def validate(root) -> bool:
    left = float('+inf')
    right = float('-inf')
    return validate_bst(root, left, right)
