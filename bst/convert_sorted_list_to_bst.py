

def sorted_list_to_bst(head):
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)

    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    n = slow.next
    slow.next = None
    if prev:
        prev.next = None
        
    node = TreeNode(slow.val)
    node.left = sorted_list_to_bst(head)
    node.right = sorted_list_to_bst(n)
    return node
