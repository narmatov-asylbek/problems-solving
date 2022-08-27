# https://leetcode.com/problems/simplify-path/

def simplify(path: str) -> str:
    stack = []
    tokens = (token for token in path.split('/'))

    for token in tokens:
        if stack and token == '..':
            stack.pop()
        elif token not in {'', '.', '..'}:
            stack.append(token)
    return '/' + '/'.join(stack)


print(simplify("/home/"))
print(simplify("/../"))
print(simplify("/home//foo/"))
