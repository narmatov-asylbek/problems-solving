


def new_node(val, left=None, right=None):
    raise NotImplementedError()


def construct(preorder: list[int], inorder: list[int]):
    if not preorder or not inorder:
        return
    root = new_node(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = construct(preorder[1: mid+1], inorder[:mid])
    root.right = construct(preorder[mid + 1:], inorder[mid+1:])
    return root
