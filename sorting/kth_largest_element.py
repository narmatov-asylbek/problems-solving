

def find_kth_largest(nums: list[int], k: int) -> int:
    
    k = len(nums) - k
    
    def quickselect(left: int, right: int) -> int:
        pivot, p = nums[right], left
        
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[right] = nums[right], nums[p]
        
        if p > k:
            return quickselect(left, p - 1)
        elif p < k:
            return quickselect(p + 1, right)
        else:
            return nums[p]
    
    return quickselect(0, len(nums) - 1)