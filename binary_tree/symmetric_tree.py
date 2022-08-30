

def helper(left, right):
    if not left and not right:
        return True
    elif not left or not right:
        return False
    elif left.val != right.val:
        return False
    return helper(left.left, right.right) and helper(left.right, right.left)

def is_symmetric(root):
    if not root:
        return True
    return helper(root.left, root.right)
