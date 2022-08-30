

class BinaryTreeNode:
    
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right



def inorder(node):
    if not node:
        return
    
    inorder(node.left)
    print(node.data)
    inorder(node.right)


def preorder(node):
    if not node:
        return
    
    print(node.data)
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)
