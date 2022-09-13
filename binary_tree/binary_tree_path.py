def new_path(path, existing) -> str:
    if not existing:
        return existing + str(path)
    
    return f"{existing}->{path}"

def tree_path(node, path, paths) -> None:
    if not node:
        return

    path = new_path(node.val, path)
    
    if not node.left and not node.right:
        paths.append(path)
        return
    tree_path(node.left, path, paths)
    tree_path(node.right, path, paths)


def binary_tree_path(root):
    paths = []
    tree_path(root, "", paths)
    return paths
    