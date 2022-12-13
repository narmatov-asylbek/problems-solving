


def fact(n: int) -> int:
    if n == 1:
        return 1
    return n * fact(n - 1)


def factorial(n: int) -> int:
    res = 1
    for j in range(1, n + 1):
         res *= j
    return res


print(fact(13), factorial(13))



def sum_prev(arr: list[int]) -> None:
    def inner(i: int) -> None:
        if i >= len(arr):
            return
        arr[i] = arr[i] + arr[i - 1]
        return inner(i + 1)
    inner(1)
    
arr = [1, 2, 3, 4, 5, 6]
sum_prev(arr)
print(arr)