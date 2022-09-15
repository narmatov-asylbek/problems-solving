import collections

def maximum_width(node) -> int:
    if not node:
        return 0
    
    queue = collections.deque([node])
    max_width = 0


    while queue:
        size = len(queue)
        max_width = max(max_width, size)
        for _ in range(size):
            level_node = queue.popleft()
            if not level_node:
                continue
            if level_node.left or level_node.right:
                queue.append(level_node.left)
                queue.append(level_node.right)
    return max_width
