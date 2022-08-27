

def is_well_formed(s: str) -> bool:
    lookup = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []

    for c in s:
        if c in lookup:
            stack.append(c)
        elif not stack or lookup[stack.pop()] != c:
            return False
    return not stack
