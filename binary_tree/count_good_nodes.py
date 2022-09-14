
def count_goods(root, current_max):
    if not root:
        return 0
    current_max = max(root.val, current_max)
    return int(root.val >= current_max) + count_goods(root.left, current_max) + count_goods(root.right, current_max)

def count_good_nodes(root) -> int:
    counter = 0

    def depth(root, curr=float('-inf')):
        if not root:
            return
        if root.val < curr:
            nonlocal counter
            counter += 1
        depth(root.left, max(root.val, curr))
        depth(root.right, max(root.val, curr))
    depth(root)
    return counter