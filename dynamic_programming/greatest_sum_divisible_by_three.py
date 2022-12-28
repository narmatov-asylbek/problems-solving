


def maximum(nums: list[int]) -> int:
    """
    >>> maximum([3, 6, 5, 1, 8])
    18
    
    >>> maximum([4])
    0
    
    >>> maximum([1, 2, 3, 4, 4])
    12
    """
    memo = {}
    def dfs(i: int, c: int) -> int:
        if (i, c) in memo:
            return memo[(i, c)]
        if i == len(nums):
            if c % 3 == 0:
                return c
            return 0
        
        n = c + nums[i]
        m = nums[i] if nums[i] % 3 == 0 else 0
        if n % 3 == 0:
            m = n
        
        memo[(i, c)] = max(m, dfs(i + 1, c), dfs(i + 1, n))
        return memo[(i, c)]
    
    return dfs(0, 0)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
