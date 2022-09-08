

class Node:

    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.prev = self.next = None


def remove(node):
    prev, next = node.prev, node.next
    prev.next, next.prev = next, prev


def insert_before(right, node):
    prev = right.prev
    prev.next = right.prev = node
    node.next, node.prev = right, prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        
        self.left.next, self.right.prev = self.right, self.left 

    def get(self, key: int) -> int:
        if key in self.cache:
            remove(self.cache[key])
            insert_before(self.right, self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            remove(self.cache[key])
        self.cache[key] = Node(key, value)
        insert_before(self.right, self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            remove(lru)
            del self.cache[lru.key]
