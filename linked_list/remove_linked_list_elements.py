class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def remove(head: ListNode, val: int) -> ListNode | None:
    dummy = ListNode(0, head)

    current = dummy

    while current and current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next