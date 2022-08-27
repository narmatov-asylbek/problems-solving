

import collections


class Queue:
    
    def __init__(self) -> None:
        self.queue = collections.deque()
    
    def enqueue(self, val):
        self.queue.append(val)
    
    def dequeue(self):
        return self.queue.popleft()

    def max(self):
        return max(self.queue)
