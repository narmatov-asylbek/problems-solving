class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(l1, l2):
    dummy = ListNode(-1)
    curr = dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next


def merge_sort(l):
    if not l or not l.next:
        return l
    
    pre = slow = fast = l

    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    
    pre.next = None
    left = merge_sort(l)
    right = merge_sort(slow)
    return merge(left, right)
