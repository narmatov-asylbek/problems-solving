from collections import namedtuple

DesCounter = namedtuple('DesCounter', ['counter', 'ancestor'])

def lowest_common(root, p, q):

    def helper(node):
        if not node:
            return DesCounter(0, None)
        left = helper(node.left)
        right = helper(node.right)
        if left.counter == 2: return left
        if right.counter == 2: return right
        current_counter = left.counter + right.counter + int(node is q) + int(node is p)
        return DesCounter(current_counter, node if current_counter == 2 else None)
    return helper(root).ancestor
