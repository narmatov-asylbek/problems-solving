import heapq

# Remove stone to minimize total
# (Int-List, int) -> int
# Given stones piles, and k, return the minimum total of piles after making k steps
def find(piles: list[int], k: int) -> int:
    """
    >>> find([5, 4, 9], 2)
    12
    
    >>> find([4, 3, 6, 7], 3)
    12
    
    >>> find([8, 10, 12, 7, 4, 3, 1, 9], 13)
    17
    """
    piles = [-x for x in piles]
    
    heapq.heapify(piles)
    for _ in range(k):
        heapq.heapreplace(piles, piles[0] // 2)
    return -sum(piles)


if __name__ == '__main__':
    import doctest
    doctest.testmod()