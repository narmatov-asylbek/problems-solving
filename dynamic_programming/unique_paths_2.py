


def unique_paths(grid: list[list[int]]) -> int:

    if grid[0][0] == 1:  # Edge case: if obstacle is located in starting position, then we cannot find path to desired location
        return 0

    grid[0][0] = 1

    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if grid[i][j] == 1:
                grid[i][j] = 0
            elif j == 0:
                grid[i][j] = grid[i - 1][j]
            elif i == 0:
                grid[i][j] = grid[i][j - 1]
            else:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[m - 1][n - 1]

print(unique_paths([[0,0,0],[0,1,0],[0,0,0]]))
print(unique_paths([[0,1],[0,0]]))
