def normalize(path: str) -> str:
    stack = []
    if path[0] == '/':
        stack.append('/')
    
    for token in (token for token in path.split('/') if token not in {'.', ''}):
        if token == '..':
            if not stack or stack[-1] == '..':
                stack.append(token)
            else:
                stack.pop()
        else:
            stack.append(token)
    
    result = '/'.join(stack)
    return result[result.startswith('//'):]
