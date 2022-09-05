

def has_path(root, target) -> bool:
    if not root:
        return False

    target -= root.val
    
    if not root.left and not root.right:
        return target == 0
    return has_path(root.left, target) or has_path(root.right, target)
