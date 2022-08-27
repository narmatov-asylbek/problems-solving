

def solution(seq) -> list:
    stack = []
    for id_, height in enumerate(seq):
        while stack and height >= stack[-1][1]:
            stack.pop()
        stack.append((id_, height))
    return [candidate[0] for candidate in reversed(stack)]
