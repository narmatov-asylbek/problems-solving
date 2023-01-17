

def min_flips(s: str) -> int:
    """
    >>> min_flips('00110')
    1
    
    >>> min_flips('010110')
    2
    
    >>> min_flips('00011000')
    2
    """
    cache = {}
    def inner(i: int, zeros: bool) -> int:
        if (i, zeros) in cache:
            return cache[(i, zeros)]
        if i == len(s):
            return 0
        
        is_zero = s[i] == '0'
        
        if zeros:
            minimum = min(inner(i + 1, zeros=True) + int(not is_zero), inner(i + 1, zeros=False))
        else:
            minimum = int(is_zero) + inner(i + 1, zeros=False)
        cache[(i, zeros)] = minimum
        return minimum
    
    return min(inner(0, True), inner(0, False))
    
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
