


# def fib(n) -> int:
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)



def fib(n) -> int:
    memo = {}
    memo[0] = 0
    memo[1] = 1
    counter = 2

    while counter <= n:
        memo[counter] = memo[counter - 1] + memo[counter - 2]
        counter += 1
    return memo[n]



print(fib(50000))