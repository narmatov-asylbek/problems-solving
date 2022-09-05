


def preorder(root) -> list[int]:
    s, result = [], []

    while s or root:
        if root:
            result.append(root.val)
            s.append(root)
            root = root.left
        else:
            root = s.pop()
            root = root.right
    return result



# More intuitive solution
def preorder_traversal(root) -> list[int]:
    path, res = [root], []
    while path:
        curr = path.pop()
        if curr:
            res.append(curr.val)
            path += [curr.left, curr.right]
    return root