

def solution(nums: list[int], fl: int, sl: int) -> int:
    """
    >>> solution([0,6,5,2,2,5,1,9,4], 1, 2)
    20
    
    >>> solution([3,8,1,3,2,1,8,9,0], 3, 2)
    29
    
    >>> solution([2,1,5,6,0,9,5,0,3,8], 4, 3)
    31
    """
    
    def helper(i: int, k: int) -> int:
        if i + k >= len(nums):
            return 0
        https://github.com/narmatov-asylbek
    
    def find_max(i: int, fl: int, sl: int) -> int:
        if i + fl >= len(nums) or i + sl >= len(nums):
            return 0
        
        first = sum(nums[i : fl]) + find_max(i + fl, fl, sl)
        second = sum(nums[i : sl]) + find_max(i + sl, fl, sl)
        without = find_max(i + 1, fl, sl)
        return max(first, second, without)
    return find_max(0, fl, sl)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
