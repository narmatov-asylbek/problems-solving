class MyQueue:

    def __init__(self):
        self.enq = []
        self.deq = []
        

    def push(self, x: int) -> None:
        self.enq.append(x)
        

    def pop(self) -> int:
        self._rebuild()
        return self.deq.pop()

    def peek(self) -> int:
        self._rebuild()
        return self.deq[-1]

    def empty(self) -> bool:
        return not (self.enq or self.deq) 
    
    def _rebuild(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())