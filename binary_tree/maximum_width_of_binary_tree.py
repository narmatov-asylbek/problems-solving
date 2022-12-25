from collections import deque

def maximum_width(node) -> int:
    queue = deque()
    queue.append([node, 1])
    max_width = 0


    while queue:
        size = len(queue)
        
        min_num = None
        for _ in range(size):
            node, num = queue.popleft()
            if min_num is None:
                min_num = num
            else:
                min_num = min(min_num, num)
                
            max_width = max(max_width, num - min_num + 1)
            
            if node.left:
                queue.append([node.left, num * 2])
            if node.right:
                queue.append([node.right, num * 2 + 1])
    return max_width
