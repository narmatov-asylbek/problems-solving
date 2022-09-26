
def helper(m, n, memo) -> int:
    if memo[m][n] != -1:
        return memo[m][n]
    if m == 0:
        res = helper(m, n - 1, memo)
    elif n == 0:
        res = helper(m - 1, n, memo)
    else:
        res = helper(m - 1, n, memo) + helper(m, n - 1, memo)
    memo[m][n] = res
    return memo[m][n]

def unique_paths(m, n):
    memo = [[-1 for _ in range(n)] for _ in range(m)]
    memo[0][0] = 1
    return helper(m - 1, n - 1, memo)


print(unique_paths(3, 7))
print(unique_paths(3, 2))
print(unique_paths(1, 1))