from list import ListNode


def merge(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1, None)
    curr = dummy
    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    if l1:
        curr.next = l1
    if l2:
        curr.next = l2
    return dummy.next


def test_merge():
    l1 = ListNode(2, ListNode(6, ListNode(8)))
    l2 = ListNode(1, ListNode(4, ListNode(12)))
    merged = merge(l1, l2)
    
    def is_sorted(l) -> bool:
        curr = l.data
        l = l.next
        while l:
            if l.data < curr:
                return False
            curr = l.data
            l = l.next
        return True
    
    print(is_sorted(merged))


if __name__ == '__main__':
    test_merge()
