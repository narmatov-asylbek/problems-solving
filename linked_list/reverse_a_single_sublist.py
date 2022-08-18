from list import ListNode



def reverse(l: ListNode, left: int, right: int) -> Optional[ListNode]:
    dummy = sublist = ListNode(-1, l)

    for _ in range(1, left):
        sublist = sublist.next

    i = sublist.next

    for _ in range(right - left):
        temp = i.next
        i.next, temp.next, sublist.next = temp.next, sublist.next, temp
    return dummy.next
