import collections

def deepest_leaves_sum(root):

    queue = collections.deque([root])

    res = 0

    while queue:
        res = 0
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()
            res += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res