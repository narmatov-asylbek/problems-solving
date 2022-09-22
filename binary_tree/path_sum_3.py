def path_sum(root, target: int) -> int:
    counter = 0
    cache = {0: 1}
    def depth(node, current, cache):
        nonlocal counter
        if not node:
            return
        current += node.val
        old = current - target
        if old in cache:
            counter += cache[old]
        
        cache[current] = cache.get(current, 0) + 1
        
        depth(node.left, current, cache)
        depth(node.right, current, cache)
        cache[current] -= 1
    depth(root, 0, cache)
    return counter