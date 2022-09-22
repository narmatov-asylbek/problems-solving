import collections

def is_even(val):
    return val % 2 == 0


def is_odd(val):
    return val % 2 != 0
    

def is_even_odd(root) -> bool:

    queue = collections.deque([root])

    is_even = True

    while queue:
        prev = None
        
        for _ in range(len(queue)):
            node = queue.popleft()
            if is_even:
                if not is_odd(node.val):
                    return False
                if prev is not None and prev >= node.val:
                    return False
            else:
                if not is_even(node.val):
                    return False
                if prev is not None and prev <= node.val:
                    return False
            prev = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        is_even = not is_even
    return True