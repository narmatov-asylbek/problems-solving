from list import ListNode


def reverse(l: ListNode) -> ListNode:
    prev = None

    while l:
        temp = l.next
        l.next = prev
        prev = l
        l = temp
    return prev

