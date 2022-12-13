
def helper(root, subroot):
    if not root and not subroot:
        return True
    if not root or not subroot:
        return False
    
    if root.val != subroot.val:
        return False
    return helper(root.left, subroot.left) and helper(root.right, subroot.right)
 
# Tree Tree -> Boolean
# Returns if subroot is subtree of root
def is_subtree(root, subroot) -> bool:
    if not root and not subroot:
        return True
    if not root:
        return False
    if not subroot:
        return True
    
    if root.val == subroot.val and helper(root, subroot):
        return True
    
    return is_subtree(root.left, subroot) or is_subtree(root.right, subroot)