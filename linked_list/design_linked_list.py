
class ListNode:
    def __init__(self, val: int, next: 'ListNode' = None):
        self.val = val
        self.next = next


def create(val: int, next: ListNode | None = None) -> ListNode:
    return ListNode(val, next)

# int -> int
# Returns val of given index
# Given 1 -> 2 -> 3, index = 1, expects 2
# get(linked_list, index)


# Add at head
# int -> None
# Adds node to the head of the linked list
# given 1 -> None, 5; expects 5 -> 1 -> None


# Add at tail
# int -> None
# Adds a node to the tail of linked list
# given 1 -> 2 -> None, 10; expects 1 -> 2 -> 10 -> None


# Add at index
# int int -> None
# Adds a node before the given index

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if 0 > index or index >= self.length:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        node = create(val)
        if self.head is None:
            self.head = node
            self.length += 1
            return
        curr = self.head
        node.next = curr
        self.head = node
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        node = create(val)
        if self.head is None:
            self.head = node
            self.length += 1
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 > index or index > self.length:
            return
        if index == self.length:
            return self.addAtTail(val)
        if index == 0:
            return self.addAtHead(val)
        
        prev = curr = self.head
        for _ in range(index):
            prev = curr
            curr = curr.next
        
        node = create(val)
        next_ = prev.next
        prev.next = node
        node.next = next_
        self.length += 1

        

    def deleteAtIndex(self, index: int) -> None:
        if 0 > index or index >= self.length:
            return
        
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return


        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next
        self.length -= 1
