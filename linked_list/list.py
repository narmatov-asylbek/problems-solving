from typing import List, Any, Optional


class ListNode:
    def __init__(self, data: Any = 0, next_node: Optional['ListNode'] = None):
        self.data = data
        self.next = next_node


# Returns node if node with given key exists
# Returns None if node not found
def search(slist: ListNode, key: Any) -> Optional[ListNode]:
    while slist and slist.data != key:
        slist = slist.next
    return slist


def insert_after(node: ListNode, new_node: ListNode) -> None:
    new_node.next = node.next
    node.next = new_node


def delete_after(node: ListNode) -> None:
    if not node.next:
        return
    node.next = node.next.next



