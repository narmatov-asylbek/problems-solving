from typing import NamedTuple


class ElementWithMin(NamedTuple):
    val: int
    min_: int


class MinStack:

    def __init__(self):
        self.stack: list[ElementWithMin] = []

    def push(self, val: int) -> None:
        min_ = val
        if len(self.stack) > 0:
            existing_min = self.stack[-1].min_
            if min_ > existing_min:
                min_ = existing_min
        node = ElementWithMin(val, min_)
        self.stack.append(node)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min_