
def lca(root):
    
    def dfs(node, depth: int):
        if not node:
            return None, 0
        if not node.left and not node.right:
            return node, depth
        
        left_node, left_depth = dfs(node.left, depth + 1)
        right_node, right_depth = dfs(node.right, depth + 1)
        
        if left_depth == right_depth:
            return node, left_depth
        if left_depth > right_depth:
            return left_node, left_depth
        else:
            return right_node, right_depth

    info = dfs(root, 0)
    return info[0]
