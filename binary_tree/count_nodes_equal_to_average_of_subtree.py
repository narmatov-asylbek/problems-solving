from typing import NamedTuple


class NodeWithValue(NamedTuple):
    amount: int
    summed: int
    


def average_of_subtree(node):
    counter = 0

    def average(node):
        if not node:
            return NodeWithValue(0, 0)
        left_amount, left_sum = average(node.left)
        right_amount, right_sum = average(node.right)

        s = left_sum +  right_sum + node.val
        a = left_amount + right_amount + 1

        avg = int(s / a)
        if avg == node.val:
            nonlocal counter
            counter += 1
        return NodeWithValue(a, s)
    average(node)
    return counter 
