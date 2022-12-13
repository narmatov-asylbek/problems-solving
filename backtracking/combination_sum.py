def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """
    >>> combination_sum([2, 3, 6, 7], 7)
    [[2, 2, 3], [7]]
    
    >>> combination_sum([2, 3, 5], 8)
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    
    >>> combination_sum([2], 1)
    []
    """
    s = []
    def helper(i: int, target: int, curr: list[int]) -> None:
        if i == len(candidates):
            return
        if target == 0:
            s.append(list(curr))
            return
        if target < 0:
            return
        
        for j in range(i, len(candidates)):
            curr.append(candidates[j])
            helper(j, target - candidates[j], list(curr))
            curr.pop()
            
                
    helper(0, target, [])
    return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()