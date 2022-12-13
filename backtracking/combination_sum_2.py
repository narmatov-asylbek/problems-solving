

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """
    >>> combination_sum([10,1,2,7,6,1,5], 8)
    [[1,1,6], [1,2,5], [1,7], [2,6]]
    
    >>> combination_sum([2, 5, 2, 1, 2], 5)
    [[1, 2, 2], [5]]
    """
    combs = []
    candidates.sort()
    
    def find(i: int, target: int, curr: list[int]) -> None:
        if target == 0:
            combs.append(list(curr))
            return
        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j - 1]:
                continue
            
            curr.append(candidates[j])
            find(j + 1, target - candidates[j], list(curr))
            curr.pop()
    
    find(0, target, [])
    return combs


if __name__ == '__main__':
    import doctest
    doctest.testmod()