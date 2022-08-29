

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.head = 0
        self.tail = 0
        self.counter = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        if self.tail == -1:
            self.tail = self.head = 0
        else:
            self.tail = (self.tail + 1) % len(self.queue)
        self.queue[self.tail] = value
        self.counter += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % len(self.queue)
        self.counter -= 1
        return True

    def Front(self) -> int:
        return self.queue[self.head] if self.head != 0 else -1

    def Rear(self) -> int:
        return self.queue[self.tail] if self.tail != 0 else -1

    def isEmpty(self) -> bool:
        return self.counter == 0

    def isFull(self) -> bool:
        return self.counter == len(self.queue)

