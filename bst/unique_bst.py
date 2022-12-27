


def count_uniques(n: int):
    """
    >>> count_uniques(3)
    5
    
    >>> count_uniques(1)
    1
    
    >>> count_uniques(2)
    2
    """
    cache = {}
    def count(n: int) -> int:
        if n <= 1:
            return 1
        if n in cache:
            return cache[n]
        
        counter = 0
        for i in range(n):
            counter += count(i) * count(n - i - 1)
        
        cache[n] = counter
        return counter
    
    return count(n)


if __name__ == '__main__':
    import doctest
    doctest.testmod()