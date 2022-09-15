

def first_greator(root, val):
    subtree, first = root, None

    while subtree:
        if subtree.data > val:
            first = subtree
            subtree = subtree.left
        else:
            subtree = subtree.right
    return first