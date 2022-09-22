

def knapsack(val: list[int], wt: list[int], weight: int) -> int:
    vals = [[0 for _ in range(weight + 1)] for _ in range(len(val) + 1)]

    for i in range(len(val) + 1):
        for j in range(weight + 1):
            if i == 0 and j == 0:
                vals[i][j] = 0
                continue
            
            if j - wt[i - 1] >= 0:
                vals[i][j] = max(vals[i - 1][j], vals[i - 1][j - wt[i - 1]] + val[i - 1])
            else:
                vals[i][j] = vals[i-1][j]
    return vals[len(val)][weight]


print(knapsack([1, 4, 5, 7], [1, 3, 4, 6], 7))