from operator import add, sub, mul, truediv

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv
}

def is_operator(op) -> bool:
    return op in operators


def is_num(el: str) -> bool:
    return el.isdigit() or el[0] == '-'

def exec(elems, op):
    l = int(elems.pop())
    k = int(elems.pop())
    res = int(operators[op]((k, l)))
    return res

def evaluate(exp):
    stack = []
    for elem in exp:
        if is_operator(elem):
            stack.append(exec(stack, elem))
        else:
            stack.append(elem)
    return stack[-1]

print(evaluate(["2","1","+","3","*"]))
print(evaluate(["4","13","5","/","+"]))
print(evaluate(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))