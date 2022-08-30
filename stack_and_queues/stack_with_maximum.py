
class StackUnderFlowError(Exception):
    pass


class MaxWithCount:
    
    def __init__(self, max, count) -> None:
        self.max, self.count = max, count


class Stack:

    def __init__(self) -> None:
        self.elements = []
        self.maximums = []
    

    def __len__(self) -> int:
        return len(self.elements)
    
    def is_empty(self) -> bool:
        return len(self) == 0

    def max(self):
        if self.is_empty():
            raise StackUnderFlowError()
        return self.maximums[-1].max

    def pop(self):
        if self.is_empty():
            raise StackUnderFlowError()
        popped = self.elements.pop()
        current_max = self.maximums[-1].max
        if popped == current_max:
            self.maximums[-1].count -= 1
            if self.maximums[-1].count == 0:
                self.maximums.pop()
        return popped
    
    def push(self, val) -> None:
        self.elements.append(val)
        maximum = MaxWithCount(val, 1)
        if len(self.maximums) == 0:
            self.maximums.append(maximum)
        else:
            current_max = self.maximums[-1].max
            if val == current_max:
                self.maximums[-1].count += 1
            elif val > current_max:
                self.maximums.append(maximum)
    
    def peek(self):
        if self.is_empty():
            raise StackUnderFlowError()
        return self.elements[-1]
