import collections

def max_level_sum(root) -> int:

    queue = collections.deque([(root, 1)])
    maximum = float('-inf')
    l = 1

    while queue:
        size = len(queue)
        level_sum = 0
        curr_level = 0

        for _ in range(size):
            n, level = queue.popleft()
            level_sum += n.val
            curr_level = level

            if n.left:
                queue.append((n.left, level + 1))
            if n.right:
                queue.append((n.right, level + 1))
        if level_sum > maximum:
            l = curr_level
            maximum = level_sum
    return l