

import collections


def level_order(root):
    if not root:
        return []
    
    result = []
    queue = collections.deque()
    queue.append(root)

    while queue:
        current_level = len(queue)
        level_values = []
        for _ in range(current_level):
            last = queue.popleft()
            level_values.append(last.val)
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)
        result.append(level_values)
    return result