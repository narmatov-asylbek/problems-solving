


def minimum_falling_path(matrix: list[list[int]]) -> int:
    """Return the minimum falling path from matrix. 
    We can go down-left or down-right or straight down path

    Args:
        matrix (list[list[int]]): Matrix of n size

    Returns:
        int: minimum falling path
        
    >>> minimum_falling_path([[2, 1, 3], [6, 5, 4], [7, 8, 9]])
    13
    
    >>> minimum_falling_path([[-19, 57], [-40, -5]])
    -59
    
    >>> minimum_falling_path([[-48]])
    -48
    """
    size = len(matrix) - 1
    memo = {}
    
    def dfs(r, c) -> int:
        if (r,c) in memo:
            return memo[(r, c)]
        if r == size and c >= 0 and c <= size:
            return matrix[r][c]
        if r < 0 or r > size or c > size or c < 0:
            return float('inf')
        
        m = matrix[r][c] + min(dfs(r + 1, c), dfs(r + 1, c - 1), dfs(r + 1, c + 1))
        memo[(r, c)] = m
        return memo[(r, c)]
    
    p = float('inf')
    for i in range(size + 1):
        p = min(p, dfs(0, i))
        
    
    return p

    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
