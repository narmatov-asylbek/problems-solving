import collections

def maximum_width(node) -> int:
    if not node:
        return 0
    
    queue = collections.deque()
    queue.append(node)
    max_width = 1


    while queue:
        size = len(queue)
        level_width = 0
        for _ in range(size):
            level_node = queue.popleft()
            if level_node.left or level_node.right:
                level_width += 2
            if level_node.left:
                queue.append(level_node.left)
            if level_node.right:
                queue.append(level_node.right)
        max_width = max(max_width, level_width)
    return max_width
