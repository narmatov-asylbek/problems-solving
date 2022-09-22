


def minimum(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == 0:
                grid[i][j] = grid[i][j] + grid[i][j - 1]
            elif j == 0:
                grid[i][j] = grid[i][j] + grid[i - 1][j]
            else:
                grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]

    return grid[-1][-1]

