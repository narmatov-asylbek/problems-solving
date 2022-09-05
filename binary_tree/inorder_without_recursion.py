from collections import deque
from os import lseek


def inorder(root) -> list[int]:
    s, result = [], []

    while s or root:
        if root:
            s.append(root.left)
            root = root.left
        else:
            root = s.pop()
            result.append(root.val)
            root = root.right
    return result