# https://leetcode.com/problems/balanced-binary-tree/
from collections import namedtuple

TreeStatusWithHeight = namedtuple('TreeStatusWithHeight', ['balanced', 'height'])

def is_balanced(tree):
    def check_balanced(tree):
        if not tree:
            return TreeStatusWithHeight(True, -1)
        left = check_balanced(tree.left)
        if not left.balanced:
            return TreeStatusWithHeight(False, 0)
        
        right = check_balanced(tree.right)
        if not right.balanced:
            return TreeStatusWithHeight(False, 0)
        
        is_balanced = abs(left.height - right.height) <= 1
        height = max(left.height, right.height) + 1
        return TreeStatusWithHeight(is_balanced, height)
    return check_balanced(tree).balanced